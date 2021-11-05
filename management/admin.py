from django.contrib import admin

from .models import Client, Contract, Order, Interview, Request, CostCategory, Cost, Vacancy, Staff


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """ Отображение клиентов в админке
    """
    list_display = ['id', 'fio', 'phone', 'email', 'manager']
    list_filter = ['manager']
    list_display_links = ['fio']
    search_fields = ['last_name', 'first_name', 'middle_name']
    fieldsets = (
        ('Менеджер', {
            'fields': ('manager',)
        }),
        ('Клиент', {
            'fields': ('first_name', 'last_name', 'middle_name', 'phone', 'email', 'city'),
        }),
        ('Паспортные данные', {
            'fields': ('passport', 'passport_issued_by', 'address',),
        }),
    )

    def fio(self, obj):
        return obj.__str__()

    fio.short_description = 'ФИО'


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """ Отображение договоров в админке
    """
    list_display = ['id', 'number', 'client', 'date']
    list_display_links = ['number']
    search_fields = ['client__last_name', 'client__first_name', 'client__middle_name', 'number']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Отображение заказов в админке
    """
    list_display = ['id', 'client', 'payed', 'course', 'date_and_time']
    list_filter = ['payed']
    search_fields = ['client', 'course']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """ Отображение вакансий в админке
    """
    list_display = ['name', 'salary', 'active', 'date']
    list_editable = ['salary', 'active']
    list_filter = ['active']


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    """ Отображение собеседований в админке
    """
    list_display = ['fio', 'vacancy', 'phone', 'result']
    list_filter = ['vacancy', 'result']
    list_editable = ['result']

    def fio(self, obj):
        return f'{obj.last_name} {obj.first_name} {obj.middle_name}'

    fio.short_description = 'ФИО'


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """ Отоборажение заявок в админке
    """
    list_display = ['client', 'type_request', 'status', 'course', 'purpose', 'result']
    list_filter = ['result', 'purpose', 'type_request', 'status']
    list_editable = ['result']


@admin.register(CostCategory)
class CostCategoryAdmin(admin.ModelAdmin):
    """ Отображение категорий затрат в админке
    """
    list_display = ['name']


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    """ Отображение затрат в админке
    """
    list_display = ['id', 'category', 'date', 'amount']
    list_filter = ['category']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    """ Отображение затрат в админке
    """
    list_display = ['id', 'username', 'full_name', 'gender', 'phone', 'user_group']
    list_filter = ['user_group']

    def full_name(self, obj):
        return obj.__str__()

    def username(self, obj):
        return obj.user.username

    full_name.short_description = 'ФИО'
    username.short_description = 'Имя пользователя'
