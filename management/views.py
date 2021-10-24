from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from management.forms import AuthForm


class MainView(View):
    """ Представление главной страницы
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/crm/auth')
        context = {'user': request.user, 'title': "CRM"}
        return render(request, 'crm/index.html', context)


class ProfileLoginView(View):
    """Идентификация и аутентификация пользователя по логину, номеру телефона и электронной почте
    """
    def get(self, request, *args, **kwargs):
        auth_form = AuthForm
        context = {
            'title': "CRM | Вход",
            'form': auth_form
        }
        return render(request, 'crm/auth.html', context)

    def post(self, request, *args, **kwargs):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/crm/')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность ввода данных')
        context = {
            'title': "CRM | Вход",
            'form': auth_form
        }
        return render(request, 'crm/auth.html', context)
