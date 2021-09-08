from django.contrib import admin

from .models import Client, Contract


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['fio', 'phone', 'email']
    search_fields = ['last_name', 'first_name', 'middle_name']
    fieldsets = (
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
    list_display = ['number', 'client', 'date']
    search_fields = ['client__last_name', 'client__first_name', 'client__middle_name', 'number']
