from django.contrib import admin
from .models import Student, Teacher, Manager, Group, Course, Lesson, Timetable, Certificate


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


@admin.register(Student)
class StudentAdmin(ProfileAdmin):
    """ Отображение списка учеников в админке """
    list_display = ['full_name', 'username', 'user_group']
    list_filter = ['group']


@admin.register(Teacher)
class TeacherAdmin(ProfileAdmin):
    """ Отображение списка преподователей в админке """
    list_display = ['full_name', 'username', 'professional_activity', 'user_group']


@admin.register(Manager)
class ManagerAdmin(ProfileAdmin):
    """ Отображение списка преподователей в админке """
    list_display = ['full_name', 'username', 'user_group']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """ Отображение списка курсов в админке """
    list_display = ['name', 'teacher']
    list_filter = ['teacher']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """ Отображение списка уоков в админке """
    list_display = ['theme', 'course']
    list_filter = ['course']


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson', 'group', 'date']
    list_display_links = ['id', 'lesson']
    list_filter = ['lesson', 'group', 'date']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'course']
    list_display_links = ['id', 'profile']
    list_filter = ['course']
