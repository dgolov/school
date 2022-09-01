from datetime import datetime

from django.db.models import Q

from mainapp.models import Student, Teacher
from management.models import Client, Request


class GroupMixin:
    """ Миксин для создания и редактирования учебных груп в CRM
    """
    @staticmethod
    def update_students_group(new_group, request) -> None:
        """ Добавляет группу в список групп выбранным студентам
        :param new_group: Созданная группа
        :param request: Объект запроса содержит в себе список студентов
        """
        students_id_list = request.POST.getlist('students')
        for student_id in students_id_list:
            try:
                student = Student.objects.get(pk=int(student_id))
                student.group_list.add(new_group)
            except Student.DoesNotExist:
                continue

    @staticmethod
    def update_teachers_group(new_group, request) -> None:
        """ Добавляет группу в список групп выбранным преподавателям
        :param new_group: Созданная группа
        :param request: Объект запроса содержит в себе список преподавателей
        """
        teachers_id_list = request.POST.getlist('teachers')
        for teacher_id in teachers_id_list:
            try:
                teacher = Teacher.objects.get(pk=int(teacher_id))
                teacher.group_list.add(new_group)
            except Student.DoesNotExist:
                continue


class CourseMixin:
    """ Миксин для создания и редактирования учебных груп в CRM
    """
    @staticmethod
    def update_teachers(new_course, request) -> None:
        teachers_id_list = request.POST.getlist('teachers')
        for teacher_id in teachers_id_list:
            teacher = Teacher.objects.get(pk=int(teacher_id))
            new_course.teachers.add(teacher)


class FilterMixin:
    """ Миксин для фильтрации в црм
    """
    def check_request_data(self, request, queryset):
        """ Проверяет параметры фильтрации
        :param request: Объект запроса
        :param queryset: Ответ от БД
        :return: Отфильтрованный объект БД
        """
        if request.GET.getlist("fio") and queryset.model == Client and len(request.GET.get("fio")) > 0:
            queryset = queryset.filter(
                Q(first_name__in=request.GET.getlist("fio")) |
                Q(middle_name__in=request.GET.getlist("fio")) |
                Q(last_name__in=request.GET.getlist("fio"))
            )
        if request.GET.getlist("status") and queryset.model == Request:
            queryset = queryset.filter(status__in=request.GET.getlist("status"))
        if request.GET.getlist("last_status") and queryset.model == Client:
            queryset = queryset.filter(last_status__in=request.GET.getlist("last_status"))
        if request.GET.get("date_from") or request.GET.get("date_to"):
            date_range = self.check_date(request)
            print(date_range)
            if date_range:
                queryset = queryset.filter(date__range=date_range)
        return queryset

    @staticmethod
    def check_date(request) -> [list, None]:
        """ Проверка фильтрации по дате по параметрам запроса date_from и date_to
            Если оба параметра отсутствуют, возвращается None,
            Если хотя бы один параметр присутствует, то возвращается диапазон дат
        :param request: объект запроса
        :return: Диапазон дат, оибо None при отсутствии параметров запроса
        """
        if len(request.GET.get("date_from")) == 0 and len(request.GET.get("date_to")) == 0:
            return None
        if len(request.GET.get("date_from")) == 0:
            date_from = '2021-01-01'
        else:
            date_from = request.GET.get("date_from")
        if len(request.GET.get("date_to")) == 0:
            date_to = datetime.now()
        else:
            date_to = request.GET.get("date_to")
        return [date_from, date_to]


class TeacherMixin:
    """ Миксин для редактирования преподавателей
    """
    @staticmethod
    def update_teacher_groups(teacher, request) -> None:
        """ Добавляет группу в список групп преподавателю
        :param teacher: преподаватель
        :param request: Объект запроса содержит в себе список курсов
        """
        group_list = request.POST.getlist('groups')
        for group in group_list:
            teacher.group_list.add(group)

    @staticmethod
    def update_teacher_courses(teacher, request) -> None:
        """ Добавляет группу в список групп преподавателю
        :param teacher: преподаватель
        :param request: Объект запроса содержит в себе список групп
        """
        course_list = request.POST.getlist('courses')
        for course in course_list:
            teacher.courses.add(course)


class StudentMixin:
    """ Миксин для редактирования студентов
    """
    @staticmethod
    def update_student_groups(student, request) -> None:
        """ Добавляет группу в список групп студента
        :param student: студен
        :param request: Объект запроса содержит в себе список курсов
        """
        group_list = request.POST.getlist('groups')
        if group_list:
            for group in group_list:
                student.group_list.add(group)

    @staticmethod
    def update_student_courses(student, request) -> None:
        """ Добавляет группу в список групп студента
        :param student: студент
        :param request: Объект запроса содержит в себе список групп
        """
        course_list = request.POST.getlist('courses')
        if course_list:
            for course in course_list:
                student.courses.add(course)
