from django.db.models import Q, Count
from rest_framework import status

from mainapp.api.serializers import MessageSerializer, GroupDialogUpdateSerializer
from mainapp.models import Photo, Profile, Dialog, DialogAttachment, Message


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
            if item_photo.for_profile.user not in profile.friends.all() and item_photo.for_profile != profile:
                return status.HTTP_403_FORBIDDEN
            if profile in item_photo.likes.all():
                item_photo.likes.remove(profile)
            else:
                item_photo.likes.add(profile)
            item_photo.save()
            return status.HTTP_201_CREATED
        except Photo.DoesNotExist:
            return status.HTTP_400_BAD_REQUEST


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
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

    def add_response_friend(self, data, item_profile):
        """ Принять дружбу """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_in.all():
            item_profile.friend_request_in.remove(profile.user)
            item_profile.followers.remove(profile.user)
            item_profile.friends.add(profile.user)
            profile.friend_request_out.remove(item_profile.user)
            profile.friends.add(item_profile.user)
            return status.HTTP_201_CREATED
        elif profile.user in item_profile.followers.all():
            item_profile.followers.remove(profile.user)
            item_profile.friends.add(profile.user)
            profile.friend_request_out.remove(item_profile.user)
            profile.friends.add(item_profile.user)
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

    def refuse_response_friend(self, data, item_profile):
        """ Оставить в подписчиках """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_in.all():
            item_profile.friend_request_in.remove(profile.user)
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

    def unsubscribe(self, data, item_profile):
        """ Отписаться """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_out.all():
            item_profile.friend_request_out.remove(profile.user)
            profile.followers.remove(item_profile.user)
            profile.friend_request_in.remove(item_profile.user)
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

    def delete_friend(self, data, item_profile):
        """ Удалить из друзей """
        profile = self.get_profile(data)
        if profile.user in item_profile.friends.all() and profile.user in item_profile.friends.all():
            item_profile.friends.remove(profile.user)
            profile.friends.remove(item_profile.user)
            profile.friend_request_out.add(item_profile.user)
            item_profile.followers.add(profile.user)
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION


class MessageMixin:
    """ Класс миксин для работы с системой личных сообщений
    """
    @staticmethod
    def read_messages(request, message_list):
        """ При открытии диалога непрочитанные сообщения становятся прочитанными """
        item_profile = request.user.profile
        for message in message_list:
            if message.from_user == item_profile:
                continue
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
        if item_profile.gender == 'm':
            message_text = f'{item_profile} создал беседу'
        else:
            message_text = f'{item_profile} создала беседу'
        if not name or not participant_list:
            return 'No data', status.HTTP_400_BAD_REQUEST
        dialog = Dialog.objects.create(name=name, is_group=True, group_founder=item_profile)
        message = Message.objects.create(
            dialog=dialog,
            from_user=item_profile,
            text=message_text,
            system_message=True)
        profiles_list = Profile.objects.filter(pk__in=participant_list)
        for profile in profiles_list:
            dialog.participants.add(profile)
        dialog.last_message = message
        dialog.save()
        return 'Created', status.HTTP_201_CREATED

    def add_user_in_dialog(self, request):
        """ Приглашение нового участника в диалог
        :param request: данные запроса (id - id диалога, user - приглашенный пользователь)
        :return: Сообщение и статус код
        """
        item_profile = request.user.profile
        data = request.data
        dialog_id = data.get('id')
        request_profiles_id_list = data.get('users')   # Список пользователей в запрое
        new_profiles_list = set()   # Итоговый список пользователей для добавления в диалог после валидации

        try:
            dialog = Dialog.objects.get(pk=dialog_id)
        except Dialog.DoesNotExist:
            return f'Dialog {dialog_id} does not Exist', status.HTTP_400_BAD_REQUEST

        if not dialog.is_group:
            return f'Dialog {dialog_id} is not a group', status.HTTP_403_FORBIDDEN

        for profile_id in request_profiles_id_list:
            try:
                profile = Profile.objects.get(pk=profile_id)
            except Profile.DoesNotExist:
                return f'Profile {profile_id} does not Exist', status.HTTP_400_BAD_REQUEST
            if profile.user not in item_profile.friends.all():
                return f'Profile {profile_id} is not your friend', status.HTTP_403_FORBIDDEN
            if profile in dialog.participants.all():
                return f'Profile {profile_id} is already in the dialog', status.HTTP_208_ALREADY_REPORTED
            new_profiles_list.add(profile)

        for new_profile in new_profiles_list:
            dialog.participants.add(new_profile)
            system_message_text = f'{item_profile} добавил пользователя - {new_profile}'
            self._send_system_message(dialog=dialog, from_user=item_profile, message=system_message_text)

        return 'Success', status.HTTP_201_CREATED

    def send_message(self, request):
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
            return f'Please input a text', status.HTTP_400_BAD_REQUEST
        try:
            to_user_id = data.pop('user_id')
            try:
                to_profile = Profile.objects.get(pk=to_user_id)
            except Profile.DoesNotExist:
                return f'Profile {to_user_id} does not Exist', status.HTTP_400_BAD_REQUEST
            if to_profile.user not in item_profile.friends.all():
                return f'Profile {to_user_id} is not your friend', status.HTTP_403_FORBIDDEN
        except KeyError:
            to_profile = None
        if not data.get('dialog'):
            if not to_profile:
                return 'You must specify a profile id or dialogue id', status.HTTP_400_BAD_REQUEST
            dialog = self._get_dialog(item_profile, to_profile)
            data['dialog'] = dialog.pk
        data['from_user'] = item_profile.pk
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return 'Created', status.HTTP_201_CREATED
        else:
            return f'Bad request Data', status.HTTP_400_BAD_REQUEST

    @staticmethod
    def _get_dialog(item_profile, to_profile):
        """ Проверяет существует ли диалог (если сообщение написанно из профиля пользователя
            Если диалог существует, то возвращается его объект,
            если не существует, то создается и возвращается новый объект диалога
        :param item_profile: Текущий пользователь (который отправляет сообщение)
        :param to_profile: Пользователь которому отправляют сообщение
        :return: id диалога
        """
        my_dialog = Dialog.objects.filter(is_group=False, participants__exact=item_profile)
        for dialog in my_dialog:
            if to_profile in dialog.participants.all():
                return dialog
        dialog = Dialog.objects.create(name=f'{item_profile} - {to_profile}')
        dialog.participants.add(item_profile)
        dialog.participants.add(to_profile)
        return dialog

    def set_chat_image(self, request, *args, **kwargs):
        """ Устанавливает новое изображение беседы
        :param request: данные запроса
        :param kwargs: кварги (в них передаем id беседы)
        :return: HTTP статус код и сообщение об успешности действия
        """
        profile = request.user.profile
        dialog_id = kwargs.get('pk')
        dialog = self.get_queryset(pk=dialog_id)
        if not dialog:
            return f'Dialog {dialog_id} does not exist', status.HTTP_400_BAD_REQUEST
        if profile not in dialog.participants.all():
            return f'The user is not a participant in the dialogue', status.HTTP_403_FORBIDDEN
        up_file = request.FILES['image']
        new_image = DialogAttachment.objects.create(file=up_file, dialog=dialog, from_user=profile)
        dialog.image = new_image
        dialog.save()
        system_message_text = f'{profile} обновил фотографию беседы.'
        self._send_system_message(dialog=dialog, from_user=profile, message=system_message_text, attachment=new_image)
        return f'Created', status.HTTP_201_CREATED

    def set_dialog_name(self, request, dialog_id, *args, **kwargs):
        """ Изменяет название групповой беседы
        :param request: данные запроса
        :param dialog_id: id группового диалога
        :return: HTTP статус код и сообщение об успешности действия
        """
        serializer = GroupDialogUpdateSerializer(data=request.data)
        if serializer.is_valid():
            dialog = self.get_queryset(pk=dialog_id)
            if not dialog:
                return f'Dialog {dialog_id} does not exist', status.HTTP_400_BAD_REQUEST
            if not dialog.is_group:
                return 'This dialog is not group', status.HTTP_405_METHOD_NOT_ALLOWED
            item_user = request.user.profile
            if item_user not in dialog.participants.all():
                return status.HTTP_403_FORBIDDEN
            dialog.name = serializer.data['name']
            dialog.save()
            system_message_text = f'{item_user} изменил название беседы.'
            self._send_system_message(dialog=dialog, from_user=item_user, message=system_message_text)
            return f'Created', status.HTTP_201_CREATED
        else:
            return f'Bad request Data', status.HTTP_400_BAD_REQUEST

    @staticmethod
    def _send_system_message(dialog, from_user, message, attachment=None):
        # Отправляем сообщение в беседу с информацией о том что фото беседы было изменено
        system_message = Message.objects.create(
            dialog=dialog,
            from_user=from_user,
            text=message,
            attachment=attachment,
            system_message=True
        )
        # Устанавливаем созданное сообщение как последнее сообщение в беседе
        dialog.last_message = system_message
        dialog.save()

    @staticmethod
    def get_queryset(pk):
        try:
            dialog = Dialog.objects.get(pk=pk)
        except Dialog.DoesNotExist:
            dialog = None
        return dialog
