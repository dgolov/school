from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.views import APIView

from mainapp.models import Photo, Profile


class ProfileManagerMixin(APIView):
    """ Миксин передающий значение текущего пользователя """
    parser_classes = (MultiPartParser, FileUploadParser,)

    def get_profile(self):
        return self.request.user.profile

    def add_photo(self, request, *args, **kwargs):
        user = self.get_profile()
        up_file = request.FILES['image']
        new_photo = Photo.objects.create(image=up_file)
        user.photos.add(new_photo)
        return new_photo

    def like_photo(self, photo_id):
        user = self.get_profile()
        try:
            item_photo = Photo.objects.get(pk=photo_id)
            if user in item_photo.likes.all():
                item_photo.likes.remove(user)
            else:
                item_photo.likes.add(user)
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
        profile = self.get_profile(data)
        in_requests = item_profile.friend_request_in.all()
        out_requests = item_profile.friend_request_out.all()
        if profile.user not in in_requests or profile.user not in out_requests:
            item_profile.friend_request_out.add(profile.user)
            profile.friend_request_in.add(item_profile.user)
            item_profile.save()
            profile.save()
            return 201
        else:
            return 203

    def add_response_friend(self, data, item_profile):
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_in.all():
            item_profile.friend_request_in.remove(profile.user)
            item_profile.friends.add(profile.user)
            profile.friend_request_out.remove(item_profile.user)
            profile.friends.add(item_profile.user)
            return 201
        else:
            return 203
