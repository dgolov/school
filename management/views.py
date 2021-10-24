from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from management.forms import AuthForm
from management.models import Client


class MainView(View):
    """ Представление главной страницы CRM
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/crm/auth')
        context = {'user': request.user, 'title': "Академия будущего"}
        return render(request, 'crm/index.html', context)


class ProfileLoginView(View):
    """Идентификация и аутентификация пользователя по логину и паролю
    """
    def get(self, request, *args, **kwargs):
        auth_form = AuthForm
        context = {
            'title': "Вход в систему",
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
            'title': "Вход в систему",
            'form': auth_form
        }
        return render(request, 'crm/auth.html', context)


class ClientsListView(ListView):
    """ Список клиентов академии
    """
    model = Client
    template_name = 'crm/clients.html'
    context_object_name = 'client_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ClientsListView, self).get_context_data(**kwargs)
        context['title'] = 'Клиенты'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Client.objects.all()
        else:
            return Client.objects.filter(manager=self.request.user)
