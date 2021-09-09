from django.contrib import admin
from django.contrib.auth.models import User

from .models import (
    Student, Teacher, EducationalManager, Group, Category, Course, Lesson, Timetable, Certificate, AcademicPerformance, Photo
)


class ProfileAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return obj.__str__()

    def username(self, obj):
        return obj.user.username

    full_name.short_description = 'ФИО'
    username.short_description = 'Имя пользователя'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """ Отображение списка групп в админке """
    list_display = ['name', 'teacher']
    search_fields = ['teacher__user__last_name', 'teacher__user__first_name', 'teacher__middle_name', 'name']


@admin.register(Student)
class StudentAdmin(ProfileAdmin):
    """ Отображение списка учеников в админке """
    # readonly_fields = ('user', 'first_name', 'last_name', 'email')
    list_display = ['full_name', 'username', 'user_group']
    list_filter = ['group']
    search_fields = ['user__last_name', 'user__first_name', 'middle_name']
    # fieldsets = (
    #     ('Обучающийся', {
    #         'fields': (
    #             'user', 'first_name', 'last_name', 'middle_name', 'phone', 'email', 'gender', 'date_of_birthday'
    #         ),
    #     }),
    # )

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    first_name.short_description = 'Имя'
    last_name.short_description = 'Фамилия'
    email.short_description = 'Электронная почта'


@admin.register(Teacher)
class TeacherAdmin(ProfileAdmin):
    """ Отображение списка преподователей в админке """
    list_display = ['full_name', 'username', 'professional_activity', 'user_group']
    search_fields = ['user__last_name', 'user__first_name', 'middle_name', 'professional_activity']


@admin.register(EducationalManager)
class ManagerAdmin(ProfileAdmin):
    """ Отображение списка преподователей в админке """
    list_display = ['full_name', 'username', 'user_group']
    search_fields = ['user__last_name', 'user__first_name', 'middle_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """ Отображение списка курсов в админке """
    list_display = ['name', 'teacher']
    list_filter = ['teacher']
    search_fields = ['teacher__user__last_name', 'teacher__user__first_name', 'teacher__middle_name', 'name']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """ Отображение списка уоков в админке """
    list_display = ['theme', 'course']
    list_filter = ['course']
    search_fields = ['theme', 'course__name']


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    """ Отображение рассписания в админке """
    list_display = ['id', 'lesson', 'group', 'date']
    list_display_links = ['id', 'lesson']
    list_filter = ['lesson', 'group', 'date']
    search_fields = ['lesson__theme', 'group__name']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """ Отображение сертификатов в админке """
    list_display = ['id', 'profile', 'course']
    list_display_links = ['id', 'profile']
    list_filter = ['course']
    search_fields = ['profile__user__last_name', 'profile__user__first_name', 'profile__middle_name', 'course__name']


@admin.register(AcademicPerformance)
class AcademicPerformanceAdmin(admin.ModelAdmin):
    """ Отображение успеваемости в админке """
    list_display = ['student', 'lesson', 'teacher', 'date']
    list_filter = ['lesson']
    list_display_links = ['student', 'lesson']
    search_fields = [
        'teacher__user__last_name', 'teacher__user__first_name', 'teacher__middle_name',
        'student__user__last_name', 'student__user__first_name', 'student__middle_name', 'lesson__theme'
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
