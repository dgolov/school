from django.contrib import admin

from .models import Client, Contract, Order


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
            'fields': ('first_name', 'last_name', 'middle_name', 'phone', 'email',),
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
