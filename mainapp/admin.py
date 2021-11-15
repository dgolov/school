from django.contrib import admin

from .models import (
    Student,
    Teacher,
    Dialog,
    DialogAttachment,
    Message,
    Group,
    Category,
    Course,
    Lesson,
    Timetable,
    Certificate,
    AcademicPerformance,
    Photo
)


admin.site.site_header = 'Администрирование Future Academy'


class ProfileAdmin(admin.ModelAdmin):
    """ Родительский класс профиля в админке
    """
    def full_name(self, obj):
        return obj.__str__()

    def username(self, obj):
        return obj.user.username

    full_name.short_description = 'ФИО'
    username.short_description = 'Имя пользователя'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """ Отображение списка групп в админке
    """
    list_display = ['id', 'name', 'teacher']
    list_display_links = ['name']
    search_fields = ['teacher__user__last_name', 'teacher__user__first_name', 'teacher__middle_name', 'name']


@admin.register(Student)
class StudentAdmin(ProfileAdmin):
    """ Отображение списка учеников в админке
    """
    # readonly_fields = ('user', 'first_name', 'last_name', 'email')
    list_display = ['id', 'full_name', 'username', 'user_group']
    list_display_links = ['full_name']
    list_filter = ['group_list']
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
    """ Отображение списка преподователей в админке
    """
    list_display = ['id', 'full_name', 'username', 'professional_activity', 'user_group']
    list_display_links = ['full_name']
    search_fields = ['user__last_name', 'user__first_name', 'middle_name', 'professional_activity']


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    """ Отображение списка диалогов в адмике
    """
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(DialogAttachment)
class DialogAttachmentAdmin(admin.ModelAdmin):
    """ Отображение списка вложений к диалогам в адмике
    """
    list_display = ['id', 'dialog', 'file']
    list_display_links = ['dialog']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """ Отображение списка личных сообщений в адмике
    """
    list_display = ['id', 'dialog', 'from_user']
    list_display_links = ['dialog']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Отображение списка категорий в адмике
    """
    list_display = ['id', 'name', 'age_group']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """ Отображение списка курсов в админке
    """
    list_display = ['id', 'name', 'teacher']
    list_display_links = ['name']
    list_filter = ['teacher']
    search_fields = ['teacher__user__last_name', 'teacher__user__first_name', 'teacher__middle_name', 'name']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """ Отображение списка уоков в админке
    """
    list_display = ['id', 'theme', 'course', 'lesson_number']
    list_display_links = ['theme']
    list_filter = ['course']
    search_fields = ['theme', 'course__name']


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    """ Отображение рассписания в админке
    """
    list_display = ['id', 'lesson', 'group', 'date', 'is_finished']
    list_display_links = ['id', 'lesson']
    list_editable = ['is_finished']
    list_filter = ['lesson', 'group', 'date']
    search_fields = ['lesson__theme', 'group__name']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """ Отображение сертификатов в админке
    """
    list_display = ['id', 'profile', 'course']
    list_display_links = ['id', 'profile']
    list_filter = ['course']
    search_fields = ['profile__user__last_name', 'profile__user__first_name', 'profile__middle_name', 'course__name']


@admin.register(AcademicPerformance)
class AcademicPerformanceAdmin(admin.ModelAdmin):
    """ Отображение успеваемости в админке
    """
    list_display = ['student', 'lesson', 'teacher', 'date']
    list_filter = ['lesson']
    list_display_links = ['student', 'lesson']
    search_fields = [
        'teacher__user__last_name', 'teacher__user__first_name', 'teacher__middle_name',
        'student__user__last_name', 'student__user__first_name', 'student__middle_name', 'lesson__theme'
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Отображение списка фотографий в адмике
    """
    list_display = ['id', 'image']
