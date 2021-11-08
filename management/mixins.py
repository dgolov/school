from mainapp.models import Student


class GroupMixin:
    """ Миксин для создания и редактирования учебных груп в CRM
    """
    @staticmethod
    def update_students_group(new_group, request) -> None:
        students_id_list = request.POST.getlist('students')
        for student_id in students_id_list:
            student = Student.objects.get(pk=int(student_id))
            student.group_list.add(new_group)
