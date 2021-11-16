from mainapp.models import Student, Teacher


class GroupMixin:
    """ Миксин для создания и редактирования учебных груп в CRM
    """
    @staticmethod
    def update_students_group(new_group, request) -> None:
        students_id_list = request.POST.getlist('students')
        for student_id in students_id_list:
            student = Student.objects.get(pk=int(student_id))
            student.group_list.add(new_group)


class CourseMixin:
    """ Миксин для создания и редактирования учебных груп в CRM
    """
    @staticmethod
    def update_teachers(new_course, request) -> None:
        teachers_id_list = request.POST.getlist('teachers')
        for teacher_id in teachers_id_list:
            teacher = Teacher.objects.get(pk=int(teacher_id))
            new_course.teachers.add(teacher)
