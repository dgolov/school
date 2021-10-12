from django.db.models import Q, Count
from rest_framework import status

from mainapp.api.serializers import MessageSerializer, GroupDialogUpdateSerializer
from mainapp.models import Photo, Profile, Dialog, DialogAttachment, Message


class PhotoManagerMixin:
    """ Класс миксин для работы с фотографиями пользователей
    """
    @staticmethod
    def add_photo(request, *args, **kwargs) -> Photo:
        """ Добавление новой фотографии
        :param request: request data
        :return: Объект фотографии
        """
        new_photo = Photo.objects.create(image=request.FILES['image'], for_profile=request.user.profile)
        request.user.profile.photos.add(new_photo)
        return new_photo

    @staticmethod
    def like_photo(request, photo_id: int, *args, **kwargs) -> int:
        """ Обработка лайка фотографии
        :param request: request data
        :param photo_id: id фотографии
        :return: статус код
        """
        try:
            item_photo = Photo.objects.get(pk=photo_id)
        except Photo.DoesNotExist:
            return status.HTTP_400_BAD_REQUEST
        if item_photo.for_profile.user not in request.user.profile.friends.all() \
                and item_photo.for_profile != request.user.profile:
            return status.HTTP_403_FORBIDDEN
        item_photo.likes.remove(request.user.profile) if request.user.profile in item_photo.likes.all() \
            else item_photo.likes.add(request.user.profile)
        return status.HTTP_201_CREATED


class AddFriendMixin:
    """ Класс миксин обработки входящих и исходящих заявок на добавление в друзья
    """
    @staticmethod
    def get_profile(data: dict) -> Profile:
        return Profile.objects.get(pk=data.get('id'))

    def add_request_friend(self, data: dict, item_profile: Profile) -> int:
        """ Предложить дружбу
        :param data: request data
        :param item_profile: Текущий пользователь
        :return: Статус код
        """
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

    def add_response_friend(self, data: dict, item_profile: Profile) -> int:
        """ Принять дружбу
        :param data: request data
        :param item_profile: Текущий пользователь
        :return: Статус код
        """
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

    def refuse_response_friend(self, data: dict, item_profile: Profile) -> int:
        """ Оставить в подписчиках
        :param data: request data
        :param item_profile: Текущий пользователь
        :return: Статус код
        """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_in.all():
            item_profile.friend_request_in.remove(profile.user)
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

    def unsubscribe(self, data: dict, item_profile: Profile) -> int:
        """ Отписаться
        :param data: request data
        :param item_profile: Текущий пользователь
        :return: Статус код
        """
        profile = self.get_profile(data)
        if profile.user in item_profile.friend_request_out.all():
            item_profile.friend_request_out.remove(profile.user)
            profile.followers.remove(item_profile.user)
            profile.friend_request_in.remove(item_profile.user)
            return status.HTTP_201_CREATED
        else:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

    def delete_friend(self, data: dict, item_profile: Profile) -> int:
        """ Удалить из друзей
        :param data: request data
        :param item_profile: Текущий пользователь
        :return: Статус код
        """
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
    def read_messages(request, message_list: list) -> None:
        """ При открытии диалога непрочитанные сообщения становятся прочитанными
        :param request: request data
        :param message_list: Список сообщений
        :return: None
        """
        for message in message_list:
            if message.from_user == request.user.profile:
                continue
            if not message.is_read:
                message.is_read = True
                message.save()

    @staticmethod
    def create_group_dialog(request) -> tuple:
        """ Создание беседы
        :param request: - данные запроса (name - имя нового диалога, participants - участники)
        :return: Сообщение и статус код
        """
        message_text = f'{request.user.profile} создал беседу' if request.user.profile.gender == 'm' \
            else f'{request.user.profile} создала беседу'
        if not request.data.get('name') or not request.data.get('participants'):
            return 'No data', status.HTTP_400_BAD_REQUEST
        dialog = Dialog.objects.create(
            name=request.data.get('name'),
            is_group=True,
            group_founder=request.user.profile
        )
        message = Message.objects.create(
            dialog=dialog,
            from_user=request.user.profile,
            text=message_text,
            system_message=True
        )
        profiles_list = Profile.objects.filter(pk__in=request.data.get('participants'))
        for profile in profiles_list:
            dialog.participants.add(profile)
        dialog.last_message = message
        dialog.save()
        return 'Created', status.HTTP_201_CREATED

    def add_user_in_dialog(self, request) -> tuple:
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

    def send_message(self, request) -> tuple:
        """ Отправка сообщений
        :param request: данные запроса (user_id - id пользователя которому отправляем сообщения, не обязательный
                                                  параметр, если его нету, используется id диалога)
                                        dialog - id диалога, не обязательный параметр, если нет используется user_id)
                                        text - Текст сообщения
        :return: Сообщение и статус код
        """
        if not request.data.get('text') or request.data.get('text') == '':
            return f'Please input a text', status.HTTP_400_BAD_REQUEST
        try:
            to_user_id = request.data.pop('user_id')
            try:
                to_profile = Profile.objects.get(pk=to_user_id)
            except Profile.DoesNotExist:
                return f'Profile {to_user_id} does not Exist', status.HTTP_400_BAD_REQUEST
            if to_profile.user not in request.user.profile.friends.all():
                return f'Profile {to_user_id} is not your friend', status.HTTP_403_FORBIDDEN
        except KeyError:
            to_profile = None
        if not request.data.get('dialog'):
            if not to_profile:
                return 'You must specify a profile id or dialogue id', status.HTTP_400_BAD_REQUEST
            dialog = self._get_dialog(request.user.profile, to_profile)
            request.data['dialog'] = dialog.pk
        request.data['from_user'] = request.user.profile.pk
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return 'Created', status.HTTP_201_CREATED
        else:
            return f'Bad request Data', status.HTTP_400_BAD_REQUEST

    @staticmethod
    def _get_dialog(item_profile: Profile, to_profile: Profile) -> Dialog:
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

    def set_chat_image(self, request, *args, **kwargs) -> tuple:
        """ Устанавливает новое изображение беседы
        :param request: данные запроса
        :param kwargs: кварги (в них передаем id беседы)
        :return: HTTP статус код и сообщение об успешности действия
        """
        dialog = self.get_queryset(pk=kwargs.get('pk'))
        if not dialog:
            return f"Dialog {kwargs.get('pk')} does not exist", status.HTTP_400_BAD_REQUEST
        if request.user.profile not in dialog.participants.all():
            return f'The user is not a participant in the dialogue', status.HTTP_403_FORBIDDEN
        new_image = DialogAttachment.objects.create(
            file=request.FILES['image'],
            dialog=dialog,
            from_user=request.user.profile
        )
        dialog.image = new_image
        dialog.save()
        system_message_text = f'{request.user.profile} обновил фотографию беседы.'
        self._send_system_message(
            dialog=dialog,
            from_user=request.user.profile,
            message=system_message_text,
            attachment=new_image
        )
        return f'Created', status.HTTP_201_CREATED

    def set_dialog_name(self, request, dialog_id: int, *args, **kwargs) -> tuple:
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
    def _send_system_message(dialog: int, from_user: int, message: str, attachment=None) -> None:
        """ Отправка системных сообщений (Пользователь добавлен в беседу, пользователь создал беседу, пользователь
        изменил фотографию беседы и тд...)
        :param dialog: id диалога
        :param from_user: id получателя
        :param message: сообщение
        :param attachment: вложение в сообщение
        :return: None
        """
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
    def get_queryset(pk: int):
        try:
            return Dialog.objects.get(pk=pk)
        except Dialog.DoesNotExist:
            return None
