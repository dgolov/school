from datetime import datetime, timedelta
from typing import Type

from django.contrib import messages
from django.db.models import Q

from mainapp.models import Student, Teacher, Course, Group, Timetable, Lesson, Achievement
from management.models import Client, Request


class GroupMixin:
    """ Миксин для создания и редактирования учебных груп в CRM
    """
    @staticmethod
    def update_students_group(new_group, students_id_list) -> None:
        """ Добавляет группу в список групп выбранным студентам
        :param new_group: Созданная группа
        :param students_id_list: Cписок студентов
        """
        for student_id in students_id_list:
            try:
                student = Student.objects.get(pk=int(student_id))
                student.group_list.add(new_group)
            except Student.DoesNotExist:
                continue

    @staticmethod
    def update_teachers_group(new_group, teachers_id_list) -> None:
        """ Добавляет группу в список групп выбранным преподавателям
        :param new_group: Созданная группа
        :param teachers_id_list: Список преподавателей
        """
        for teacher_id in teachers_id_list:
            try:
                teacher = Teacher.objects.get(pk=int(teacher_id))
                teacher.group_list.add(new_group)
            except Student.DoesNotExist:
                continue

    @staticmethod
    def delete_student(request, group, student_id) -> None:
        """ Удаление группы из списка групп студена
        :param request: объект запроса
        :param group: объект студента
        :param student_id: id удаляемой группы
        """
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Ошибка удаления студента.')
            return
        student.group_list.remove(group)
        messages.add_message(request, messages.SUCCESS, f'Студент {student} успешно удален из группы.')

    @staticmethod
    def delete_course(request, group, course_id) -> None:
        """ Удаление курса из списка курсов студента
        :param request: объект запроса
        :param group: объект группы
        :param course_id: id удаляемого курса
        """
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Ошибка удаления курса.')
            return
        group.courses.remove(course)
        messages.add_message(request, messages.SUCCESS, f'Курс {course} успешно удален.')

    @staticmethod
    def update_courses_group(new_group, courses_id_list) -> None:
        """ Добавляет список курсов в группу
        :param new_group: Созданная группа
        :param courses_id_list: Список курсов
        """
        for courses_id in courses_id_list:
            try:
                course = Course.objects.get(pk=int(courses_id))
                new_group.courses.add(course)
            except Course.DoesNotExist:
                continue


class CourseMixin:
    """ Миксин для создания и редактирования учебных груп в CRM
    """
    @staticmethod
    def update_teachers(new_course, request) -> None:
        teachers_id_list = request.POST.getlist('teachers')
        for teacher_id in teachers_id_list:
            try:
                teacher = Teacher.objects.get(pk=int(teacher_id))
            except Teacher.DoesNotExist:
                continue
            new_course.teachers.add(teacher)
            teacher.courses.add(new_course)


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
        if request.GET.get("result"):
            queryset = queryset.filter(result=request.GET.get("result"))
        if request.GET.getlist("last_status") and queryset.model == Client:
            queryset = queryset.filter(last_status__in=request.GET.getlist("last_status"))
        if request.GET.get("date_from") or request.GET.get("date_to"):
            date_range = self.check_date(request)
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
        try:
            group_list = request.POST.getlist('groups')
            if group_list:
                for group in group_list:
                    teacher.group_list.add(group)
                messages.add_message(request, messages.SUCCESS, 'Группы успешно добавлены.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Ошибка добавления групп.')
        return

    @staticmethod
    def update_teacher_courses(teacher, request) -> None:
        """ Добавляет группу в список групп преподавателю
        :param teacher: преподаватель
        :param request: Объект запроса содержит в себе список групп
        """
        try:
            course_list = request.POST.getlist('courses')
            if course_list:
                for course in course_list:
                    teacher.courses.add(course)
                    course.teachers.add(teacher)
                messages.add_message(request, messages.SUCCESS, 'Курсы успешно добавлены.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Ошибка добавления курсов.')
        return


class StudentMixin:
    """ Миксин для редактирования студентов
    """
    @staticmethod
    def update_student_groups(student, request) -> None:
        """ Добавляет группу в список групп студента
        :param student: студен
        :param request: Объект запроса содержит в себе список курсов
        """
        try:
            group_list = request.POST.getlist('groups')
            if group_list:
                for group in group_list:
                    student.group_list.add(group)
                messages.add_message(request, messages.SUCCESS, 'Группы успешно добавлены.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Ошибка добавления групп.')
        return

    @staticmethod
    def update_student_courses(student, request) -> None:
        """ Добавляет группу в список групп студента
        :param student: студент
        :param request: Объект запроса содержит в себе список групп
        """
        try:
            course_list = request.POST.getlist('courses')
            if course_list:
                for course in course_list:
                    student.courses.add(course)
                messages.add_message(request, messages.SUCCESS, 'Курсы успешно добавлены.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Ошибка добавления курсов.')
        return

    @staticmethod
    def update_student_achievements(student, request) -> None:
        """ Добавляет ачивку в список ачивок студента
        :param student: студент
        :param request: Объект запроса содержит в себе список ачивок
        """
        try:
            achievement_list = request.POST.getlist('achievements')
            if achievement_list:
                for achievement in achievement_list:
                    student.achievement.add(achievement)
                messages.add_message(request, messages.SUCCESS, 'Ачивки успешно добавлены.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Ошибка добавления ачивок.')
        return

    @staticmethod
    def delete_course(request, student, course_id) -> None:
        """ Удаление курса из списка курсов студента
        :param request: объект запроса
        :param student: объект студента
        :param course_id: id удаляемого курса
        """
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Ошибка удаления курса.')
            return
        student.courses.remove(course)
        messages.add_message(request, messages.SUCCESS, f'Курс {course} успешно удален.')

    @staticmethod
    def delete_group(request, student, group_id) -> None:
        """ Удаление группы из списка групп студена
        :param request: объект запроса
        :param student: объект студента
        :param group_id: id удаляемой группы
        """
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Ошибка удаления группы.')
            return
        student.group_list.remove(group)
        messages.add_message(request, messages.SUCCESS, f'Группа {group} успешно удалена.')

    @staticmethod
    def delete_achievement(request, student, achievement_id) -> None:
        """ Удаление ачивки из списка групп студена
        :param request: объект запроса
        :param student: объект студента
        :param achievement_id: id удаляемой ачивки
        """
        try:
            achievement = Achievement.objects.get(pk=achievement_id)
        except Achievement.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Ошибка удаления ачивки.')
            return
        student.achievement.remove(achievement)
        messages.add_message(request, messages.SUCCESS, f'Ачивка {achievement} успешно удалена.')


class TimeTAbleMixin:
    """ Миксин расписания уроков
    """
    date = None
    days_of_week_list = None
    lesson = None
    group = None
    material_link = None
    timetable_object = None
    file = None
    teacher = None

    def _save_timetable(self):
        """ сохранение расписания """
        if self.timetable_object:
            return self._update_timetable()
        new_timetable = Timetable()
        new_timetable.date = self.date
        new_timetable.group = self.group
        new_timetable.lesson = self.lesson
        new_timetable.teacher = self.teacher
        new_timetable.subject = self.lesson.theme
        if self.material_link:
            new_timetable.material_link = self.material_link
        if self.file:
            new_timetable.material = self.file
        new_timetable.save()

    def _update_timetable(self):
        """ обновление расписания """
        self.timetable_object.date = self.date
        self.timetable_object.group = self.group
        self.timetable_object.lesson = self.lesson
        self.timetable_object.teacher = self.teacher
        self.timetable_object.subject = self.lesson.theme
        if self.material_link:
            self.timetable_object.material_link = self.material_link
        if self.file:
            self.timetable_object.material = self.file
        self.timetable_object.save()

    @staticmethod
    def _get_lesson(lesson_id):
        if not lesson_id:
            return None
        try:
            return Lesson.objects.get(pk=lesson_id)
        except Lesson.DoesNotExist:
            return None

    @staticmethod
    def _get_group(group_id):
        if not group_id:
            return None
        try:
            return Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return None

    @staticmethod
    def _get_teacher(teacher_id):
        if not teacher_id:
            return None
        try:
            return Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return None

    def processed_timetable(self, form, request, timetable_object=None):
        """ главная функция, обновляет, добавляет пирион записей, добавляет одиночные записи
        :param form: заполненая форма
        :param request: объект запроса
        :param timetable_object: объект расписания (для обновления)
        :return: None
        """
        self.date = form.cleaned_data.get('date', None)
        self.days_of_week_list = request.POST.getlist('day_of_week', None)
        self.material_link = form.cleaned_data.get('material_link', None)
        self.timetable_object = timetable_object

        self.lesson = self._get_lesson(lesson_id=request.POST.get('lesson', None))
        if not self.lesson:
            messages.add_message(request, messages.ERROR, 'Ошибка создания записи. Не указана тема урока.')
            return

        self.group = self._get_group(group_id=request.POST.get('group', None))
        if not self.group:
            messages.add_message(request, messages.ERROR, 'Ошибка создания записи. Группы не существует.')
            return

        self.teacher = self._get_teacher(teacher_id=request.POST.get('teacher', None))
        if not self.teacher:
            messages.add_message(request, messages.ERROR, 'Ошибка создания записи. Преподавателя не существует.')
            return

        if not self.days_of_week_list and form.is_valid():
            self.file = request.FILES.get('file', None)
            try:
                self._save_timetable()
            except Exception as e:
                messages.add_message(
                    request, messages.ERROR, 'Ошибка создания записи. Введены некорректные данные.'
                )

        elif self.days_of_week_list:
            end_date = datetime.strptime(request.POST.get('end_date'), "%Y-%m-%d")
            while self.date.timestamp() <= end_date.timestamp():
                if str(self.date.strftime("%A")).lower() in self.days_of_week_list:
                    try:
                        self._save_timetable()
                    except Exception as e:
                        messages.add_message(
                            request, messages.ERROR, 'Ошибка создания записи. Введены некорректные данные.'
                        )
                self.date += timedelta(days=1)

        else:
            messages.add_message(request, messages.ERROR, 'Ошибка создания записи. Введены некорректные данные.')


class StatisticMixin:
    """ Миксин для подсчета статистики по студентам и преподавателям
    """
    @staticmethod
    def get_academic_performance_average(academic_performance, academic_performance_count: int) -> Type[int or str]:
        """ Высчитывает средний бал успеваемости по студенту или по преподавателю
            исходя из полученых или поставленых оценок
        :param academic_performance: Оценки отфильтрованные по пользователю
        :param academic_performance_count: Количество оценок по пользователю
        :return: Средний бал
        """
        academic_performance_sum = 0

        print(academic_performance)

        print(1)
        for item in academic_performance:
            try:
                academic_performance_sum += item.grade
            except TypeError:
                academic_performance_count -= 1
                continue

        try:
            return academic_performance_sum / academic_performance_count
        except Exception as e:
            print(e)
            return 'Отсутствует'

    @staticmethod
    def get_average_statistic(academic_performance, time_table_count: int) -> Type[dict or None]:
        """ Вычисляет статистику по посещаемости: количество пропусков и опозданий и процент пропусков и опозданий
        :param academic_performance: Оценки отфильтрованные по студенту (посещаемость входит в успеваемость)
        :param time_table_count: Количество занятий по студенту
        :return: словарь статистики
        """
        average_statistic = {
            'late_count': 0,
            'absent_count': 0,
            'percent_late': 0,
            'percent_absent': 0,
        }
        if not time_table_count or not academic_performance:
            return average_statistic

        try:
            for item in academic_performance:
                if item.late:
                    average_statistic['late_count'] += 1
                elif item.absent:
                    average_statistic['absent_count'] += 1
        except Exception as e:
            return None

        average_statistic['percent_late'] = average_statistic['late_count'] / time_table_count * 100
        average_statistic['percent_absent'] = average_statistic['absent_count'] / time_table_count * 100

        return average_statistic

