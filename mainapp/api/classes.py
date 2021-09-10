from mainapp.models import Course


class BuyingCourseManager:
    """ Реализация оплаты курса """

    def get_buy_status(self, request):
        profile = request.user.profile
        if profile.user_group != "student":
            return 403  # Покупают курсы только с аккаунтов студентов
        student = profile.student
        data = request.data
        course_id = data.get('id')
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return 400
        if course in student.courses.all():
            return 208
        if self.get_paid(course.price):
            student.courses.add(course)
            return 201

    @staticmethod
    def get_paid(price):
        """ Реализация взаимодействия с платежной системой """
        # TODO определиться с платежной системой и реализовать функцию оплаты
        return True
