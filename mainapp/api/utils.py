from mainapp.api.serializers import ProfileSerializer
from mainapp.models import Course, Group, Lesson
from rest_framework import status

import os


def get_serializer_to_display_the_profile(request, obj, detail_serializer_class):
    """ Выбор серилизатора для режима отображения профиля.
    Если пользователь в друзьях, то используется детальный серилизатор, иначе серилизатор с не полной информацией.
    Информация о профиле показывается только друзьям пользователя
    """
    if obj.user in request.user.profile.friends.all() and request.user in obj.friends.all():
        serializer = detail_serializer_class(obj, many=False)
    else:
        serializer = ProfileSerializer(obj, many=False)

    return serializer


def check_correct_data_for_add_in_timetable(item_profile, data):
    """ Проверка данных на добавление урока в рассписание
    Данные преподавателя который редактирует рассписание должно совпадать с данными отправленными на сервер
    """
    try:
        lesson = Lesson.objects.get(pk=data['lesson'])
    except Course.DoesNotExist:
        return status.HTTP_400_BAD_REQUEST
    try:
        group = Group.objects.get(pk=data['group'])
    except Group.DoesNotExist:
        return status.HTTP_400_BAD_REQUEST

    status_code = status.HTTP_403_FORBIDDEN
    if item_profile.user_group == 'teacher' and \
            (lesson.course.teacher.pk == item_profile.pk or group.teacher.pk == item_profile.pk):
        status_code = status.HTTP_202_ACCEPTED
    elif item_profile.user_group == 'manager' and group.manager.pk == item_profile.pk:
        status_code = status.HTTP_202_ACCEPTED

    return status_code


def delete_file(path):
    """ Удаление файлов на сервере """
    path = path[1:]

    if os.path.exists(path):
        os.remove(path)
        return 1
    else:
        return 0


def get_student_group_name_list(student):
    """ Получене списка имен групп у студента """
    group_name_list = []

    for group in student.group_list.all():
        group_name_list.append(group.name)

    return group_name_list
