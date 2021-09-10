from mainapp.models import Photo, Profile


class PhotoManagerMixin:
    """ Класс миксин для работы с фотографиями пользователей
    """
    @staticmethod
    def add_photo(request, *args, **kwargs):
        profile = request.user.profile
        up_file = request.FILES['image']
        new_photo = Photo.objects.create(image=up_file, for_profile=profile)
        profile.photos.add(new_photo)
        return new_photo

    @staticmethod
    def like_photo(request, photo_id, *args, **kwargs):
        profile = request.user.profile
        try:
            item_photo = Photo.objects.get(pk=photo_id)
            if item_photo.for_profile.user not in profile.friends.all():
                return 403
            if profile in item_photo.likes.all():
                item_photo.likes.remove(profile)
            else:
                item_photo.likes.add(profile)
            item_photo.save()
            return 201
        except Photo.DoesNotExist:
            return 400


class AddFriendMixin:
    """ Класс миксин обработки входящих и исходящих заявок на добавление в друзья """
    @staticmethod
    def get_profile(data):
        user_id = data.get('id')
        return Profile.objects.get(pk=user_id)

    def add_request_friend(self, data, item_profile):
        """ Предложить дружбу """
        profile = self.get_profile(data)
        in_request_friend_list = item_profile.friend_request_in.all()
        out_request_friend_list = item_profile.friend_request_out.all()
        if profile.user not in in_request_friend_list or profile.user not in out_request_friend_list:
            item_profile.friend_request_out.add(profile.user)
            profile.friend_request_in.add(item_profile.user)
            profile.followers.add(item_profile.user)
            return 201
        else:
            return 203

    def add_response_friend(self, data, item_profile):
        """ Принять дружбу """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_in.all():
            item_profile.friend_request_in.remove(profile.user)
            item_profile.followers.remove(profile.user)
            item_profile.friends.add(profile.user)
            profile.friend_request_out.remove(item_profile.user)
            profile.friends.add(item_profile.user)
            return 201
        elif profile.user in item_profile.followers.all():
            item_profile.followers.remove(profile.user)
            item_profile.friends.add(profile.user)
            profile.friend_request_out.remove(item_profile.user)
            profile.friends.add(item_profile.user)
            return 201
        else:
            return 203

    def refuse_response_friend(self, data, item_profile):
        """ Оставить в подписчиках """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_in.all():
            item_profile.friend_request_in.remove(profile.user)
            return 201
        else:
            return 203

    def unsubscribe(self, data, item_profile):
        """ Отписаться """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_out.all():
            item_profile.friend_request_out.remove(profile.user)
            profile.followers.remove(item_profile.user)
            profile.friend_request_in.remove(item_profile.user)
            return 201
        else:
            return 203

    def delete_friend(self, data, item_profile):
        """ Удалить из друзей """
        profile = self.get_profile(data)
        if profile.user in item_profile.friends.all() and profile.user in item_profile.friends.all():
            item_profile.friends.remove(profile.user)
            profile.friends.remove(item_profile.user)
            profile.friend_request_out.add(item_profile.user)
            item_profile.followers.add(profile.user)
            return 201
        else:
            return 203
