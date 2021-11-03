from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from management.forms import AuthForm, CreateClientForm
from management.models import Client, Contract, Order, Vacancy, Interview, Request, Cost

from mainapp.models import Course, Lesson, Timetable, AcademicPerformance


class MainView(View):
    """ Представление главной страницы CRM
    """
    @staticmethod
    def get(request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/api/crm/auth')
        return render(request, 'crm/index.html', {'user': request.user, 'title': "Академия будущего"})


class ProfileLoginView(View):
    """Идентификация и аутентификация пользователя по логину и паролю в CRM
    """
    @staticmethod
    def get(request, *args, **kwargs):
        auth_form = AuthForm
        return render(request, 'crm/authentication-login.html', {'title': "Вход в систему", 'form': auth_form})

    @staticmethod
    def post(request, *args, **kwargs):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            user = authenticate(
                username=auth_form.cleaned_data['username'],
                password=auth_form.cleaned_data['password']
            )
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/api/crm/')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность ввода данных')
        return render(request, 'crm/authentication-login.html', {'title': "Вход в систему", 'form': auth_form})


class ClientsListView(ListView):
    """ Список клиентов академии в CRM
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


class ClientDetailView(DetailView):
    """ Детальное представление клиента в CRM
    """
    model = Client
    template_name = 'crm/client_detail.html'
    context_object_name = 'client'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        context['contracts'] = Contract.objects.filter(client=self.get_object())
        context['orders'] = Order.objects.filter(client=self.get_object())
        context['requests'] = Request.objects.filter(client=self.get_object())
        return context


class CreateClientView(View):
    """ Регистрация нового клиента в CRM
    """
    @staticmethod
    def get(request, *args, **kwargs):
        form = CreateClientForm()
        return render(request, 'crm/create_client.html', {'form': form, 'title': 'Регистрация нового клиента'})

    @staticmethod
    def post(request, *args, **kwargs):
        form = CreateClientForm(request.POST)
        if form.is_valid():
            new_client = form.save()
            new_client.manager = request.user
            new_client.save()
        return HttpResponseRedirect('/api/crm/clients')


class ContractListView(ListView):
    """ Список договоров в CRM
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


class ContractDetailView(DetailView):
    """ Детальное представление договора в CRM
    """
    model = Contract
    template_name = 'crm/contract_detail.html'
    context_object_name = 'contract'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContractDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class OrderListView(ListView):
    """ Список заказов в CRM
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


class OrderDetailView(DetailView):
    """ Детальное представление заказа в CRM
    """
    model = Order
    template_name = 'crm/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class RequestListView(ListView):
    """ Список заявок в CRM
    """
    model = Request
    template_name = 'crm/request_list.html'
    context_object_name = 'request_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RequestListView, self).get_context_data(**kwargs)
        context['title'] = 'Заявки'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Request.objects.all() if self.request.user.is_staff else None


class RequestDetailView(DetailView):
    """ Детальное представление заявки в CRM
    """
    model = Request
    template_name = 'crm/request_detail.html'
    context_object_name = 'request'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RequestDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class VacancyListView(ListView):
    """ Список вакансий в CRM
    """
    model = Vacancy
    template_name = 'crm/vacancy_list.html'
    context_object_name = 'vacancy_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['title'] = 'Вакансии'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Vacancy.objects.all() if self.request.user.is_staff else None


class VacancyDetailView(DetailView):
    """ Детальное представление вакансии в CRM
    """
    model = Vacancy
    template_name = 'crm/vacancy_detail.html'
    context_object_name = 'vacancy'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class InterviewListView(ListView):
    """ Список соеседований в CRM
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


class InterviewDetailView(DetailView):
    """ Детальное представление вакансии в CRM
    """
    model = Interview
    template_name = 'crm/interview_detail.html'
    context_object_name = 'interview'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InterviewDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class CourseListView(ListView):
    """ Список курсов в CRM
    """
    model = Course
    template_name = 'crm/course_list.html'
    context_object_name = 'course_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['title'] = 'Курсы'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Course.objects.all() if self.request.user.is_staff else None


class CourseDetailView(DetailView):
    """ Детальное представление курса в CRM
    """
    model = Course
    template_name = 'crm/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        context['lesson_list'] = Lesson.objects.filter(course=self.get_object())
        return context


class TimeTableListView(ListView):
    """ Рассписание в CRM
    """
    model = Timetable
    template_name = 'crm/time_table_list.html'
    context_object_name = 'time_table_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TimeTableListView, self).get_context_data(**kwargs)
        context['title'] = 'Рассписание'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Timetable.objects.all() if self.request.user.is_staff else None


class AcademicPerformanceListView(ListView):
    """ Успевоемость в CRM
    """
    model = AcademicPerformance
    template_name = 'crm/academic_performance_list.html'
    context_object_name = 'academic_performance_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AcademicPerformanceListView, self).get_context_data(**kwargs)
        context['title'] = 'Успеваемость'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return AcademicPerformance.objects.all() if self.request.user.is_staff else None
