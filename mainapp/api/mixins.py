from mainapp.api.serializers import MessageSerializer
from mainapp.models import Photo, Profile, Dialog


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
    """ Класс миксин обработки входящих и исходящих заявок на добавление в друзья
    """
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


class MessageMixin:
    """ Класс миксин для работы с системой личных сообщений
    """
    @staticmethod
    def read_messages(message_list):
        """ При открытии диалога непрочитанные сообщения становятся прочитанными """
        for message in message_list:
            if not message.is_read:
                message.is_read = True
                message.save()

    @staticmethod
    def create_group_dialog(request):
        """ Создание беседы
        :param request: - данные запроса (name - имя нового диалога, participants - участники)
        :return: Сообщение и статус код
        """
        item_profile = request.user.profile
        data = request.data
        name = data.get('name')
        participant_list = data.get('participants')
        if not name or not participant_list:
            return 'No data', 400
        dialog = Dialog.objects.create(name=name, is_group=True, group_founder=item_profile)
        profiles_list = Profile.objects.filter(pk__in=participant_list)
        for profile in profiles_list:
            dialog.participants.add(profile)
        return 'Created', 201

    @staticmethod
    def add_user_in_dialog(request):
        """ Приглашение нового участника в диалог
        :param request: данные запроса (id - id диалога, user - приглашенный пользователь)
        :return: Сообщение и статус код
        """
        item_profile = request.user.profile
        data = request.data
        dialog_id = data.get('id')
        profile_id = data.get('user')

        try:
            dialog = Dialog.objects.get(pk=dialog_id)
        except Dialog.DoesNotExist:
            return f'Dialog {dialog_id} does not Exist', 400

        if not dialog.is_group:
            return f'Dialog {dialog_id} is not a group', 403

        try:
            profile = Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist:
            return f'Profile {profile_id} does not Exist', 400

        if profile.user not in item_profile.friends.all():
            return f'Profile {profile_id} is not your friend', 403
        if profile in dialog.participants.all():
            return f'Profile {profile_id} is already in the dialog', 208

        dialog.participants.add(profile)
        return 'Success', 201

    @staticmethod
    def send_message(request):
        """ Отправка сообщений
        :param request: данные запроса (user_id - id пользователя которому отправляем сообщения, не обязательный
                                                  параметр, если его нету, используется id диалога)
                                        dialog - id диалога, не обязательный параметр, если нет используется user_id)
                                        text - Текст сообщения
        :return: Сообщение и статус код
        """
        item_profile = request.user.profile
        data = request.data
        if not data.get('text') or data.get('text') == '':
            return f'Please input a text', 400
        try:
            to_user_id = data.pop('user_id')
            try:
                to_profile = Profile.objects.get(pk=to_user_id)
            except Profile.DoesNotExist:
                return f'Profile {to_user_id} does not Exist', 400
            if to_profile.user not in item_profile.friends.all():
                return f'Profile {to_user_id} is not your friend', 403
        except KeyError:
            to_profile = None
        if not data.get('dialog'):
            if not to_profile:
                return 'You must specify a profile id or dialogue id', 400
            new_dialog = Dialog.objects.create(name=f'{item_profile} - {to_profile}')
            new_dialog.participants.add(item_profile)
            new_dialog.participants.add(to_profile)
            data['dialog'] = new_dialog.pk
        data['from_user'] = item_profile.pk
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return 'Created', 201

