from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from management.forms import AuthForm
from management.models import Client, Contract, Order, Interview, Request, Cost


class MainView(View):
    """ Представление главной страницы CRM
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/api/crm/auth')
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
        return render(request, 'crm/authentication-login.html', context)

    def post(self, request, *args, **kwargs):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/api/crm/')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность ввода данных')
        context = {
            'title': "Вход в систему",
            'form': auth_form
        }
        return render(request, 'crm/authentication-login.html', context)


class ClientsListView(ListView):
    """ Список клиентов академии
    """
    model = Client
    template_name = 'crm/clients_list.html'
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


class ContractListView(ListView):
    """ Список договоров
    """
    model = Contract
    template_name = 'crm/contracts_list.html'
    context_object_name = 'contracts_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContractListView, self).get_context_data(**kwargs)
        context['title'] = 'Договора'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        return Contract.objects.all() if self.request.user.is_staff else None


class InterviewListView(ListView):
    """ Список соеседований
    """
    model = Interview
    template_name = 'crm/interview_list.html'
    context_object_name = 'interview_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InterviewListView, self).get_context_data(**kwargs)
        context['title'] = 'Собеседования'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Interview.objects.all()
        else:
            return Interview.objects.filter(user=self.request.user)


class OrderListView(ListView):
    """ Список заказов
    """
    model = Order
    template_name = 'crm/order_list.html'
    context_object_name = 'order_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['title'] = 'Заказы'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all() if self.request.user.is_staff else None
