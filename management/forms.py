from django import forms

from mainapp.models import Course
from management.models import Client, Contract, Order, Request, Vacancy, Interview


class AuthForm(forms.Form):
    """ Форма входа пользователя в CRM
    """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Логин, телефон или email...'}
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль...'}
        )
    )


class CreateClientForm(forms.ModelForm):
    """ Форма регистрации нового клиента в CRM
    """
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите фамилию клиента...'}
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя клиента...'}
        )
    )
    middle_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите отчество клиента...'}
        )
    )
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона клиента...'}
        )
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите email клиента...'}
        )
    )
    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите город клиента...'}
        )
    )
    passport = forms.CharField(
        label='Серия и номер паспорта',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите серию и номер паспорта клиента...'}
        )
    )
    passport_issued_by = forms.CharField(
        label='Кем выдан',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите кем выдан паспорт...'}
        )
    )
    address = forms.CharField(
        label='Адрес прописка',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите адрес прописки клиента...'}
        )
    )

    class Meta:
        model = Client
        fields = (
            'first_name', 'last_name', 'middle_name',
            'phone', 'email', 'city',
            'passport', 'passport_issued_by', 'address'
        )


class CreateContractForm(forms.ModelForm):
    """ Форма регистрации нового контракта в CRM
    """
    number = forms.CharField(
        label='Номер договора',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите номер договора...'}
        )
    )
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Введите комментарий менеджера...'}
        )
    )

    class Meta:
        model = Contract
        fields = ('number', 'client', 'course', 'comment')
