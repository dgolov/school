from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from django.db.models.functions import TruncMonth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView

from management.classes import PaymentManager
from management import forms
from management.models import (
    Client,
    Contract,
    Order,
    Vacancy,
    Interview,
    Request,
    Cost,
    CostCategory,
    Staff
)
from management.mixins import GroupMixin, CourseMixin, FilterMixin, TeacherMixin
from mainapp.models import Course, Lesson, Timetable, AcademicPerformance, Teacher, Student, Group

from datetime import datetime, timedelta


class MainView(View):
    """ Представление главной страницы CRM
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/api/crm/auth')
        context = self.get_context_data()
        return render(request, 'crm/index.html', context)

    def get_context_data(self):
        return {
            'user': self.request.user,
            'title': "Академия будущего",
            'orders_count': Order.objects.filter(payed=True).count(),
            'students_count': Student.objects.all().count(),
            'requests_count': Request.objects.all().count(),
            'contracts_count': Contract.objects.all().count(),
            'orders_groups': Order.objects.filter(payed=True, date_and_time__year=datetime.now().year).annotate(
                date=TruncMonth('date_and_time')).values('date').annotate(total_price=Sum('price')),
        }


class ProfileLoginView(View):
    """Идентификация и аутентификация пользователя по логину и паролю в CRM
    """
    @staticmethod
    def get(request, *args, **kwargs):
        auth_form = forms.AuthForm
        return render(request, 'crm/authentication-login.html', {'title': "Вход в систему", 'form': auth_form})

    @staticmethod
    def post(request, *args, **kwargs):
        auth_form = forms.AuthForm(request.POST)
        if auth_form.is_valid():
            user = authenticate(
                username=auth_form.cleaned_data['username'],
                password=auth_form.cleaned_data['password']
            )
            if user:
                if not user.is_staff:
                    return HttpResponse('Нет доступа', status=403)
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/api/crm/')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность ввода данных')
        return render(request, 'crm/authentication-login.html', {'title': "Вход в систему", 'form': auth_form})


class ClientsListView(FilterMixin, ListView):
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
        if self.request.user.staff.user_group == 'admin':
            queryset = Client.objects.all()
        elif self.request.user.staff.user_group == 'sale_manager':
            queryset = Client.objects.filter(manager=self.request.user.staff)
        else:
            return None
        return self.check_request_data(request=self.request, queryset=queryset)


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
        context['contracts'] = self.get_object().client_contract.all()
        context['orders'] = Order.objects.filter(client=self.get_object())
        context['requests'] = Request.objects.filter(client=self.get_object())
        return context


class CreateClientView(CreateView):
    """ Регистрация нового клиента в CRM
    """
    template_name = 'crm/create_client.html'
    form_class = forms.ClientForm

    def get_context_data(self, **kwargs):
        context = super(CreateClientView, self).get_context_data()
        context['title'] = 'Регистрация нового клиента'
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.manager = self.request.user.staff
            new_client.save()
        return HttpResponseRedirect('/api/crm/clients')


class UpdateClientView(UpdateView):
    """ Редактирование клиента в CRM
    """
    model = Client
    template_name = 'crm/update_client.html'
    form_class = forms.ClientForm
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super(UpdateClientView, self).get_context_data()
        context['title'] = 'Редактирование клиента'
        return context

    def get_success_url(self):
        return f'/api/crm/clients/{self.get_object().pk}'


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
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'sale_manager':
            return Contract.objects.all()
        else:
            return None


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


class CreateContractView(CreateView):
    """ Регистрация нового договора в CRM
    """
    template_name = 'crm/create_contract.html'
    form_class = forms.CreateContractForm

    def get_context_data(self, **kwargs):
        context = super(CreateContractView, self).get_context_data()
        context['title'] = 'Добавление нового договора'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/api/crm/contracts')


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
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'sale_manager':
            return Order.objects.all()
        else:
            return None


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


class CreateOrderView(CreateView):
    """ Регистрация нового заказа в CRM
    """
    template_name = 'crm/create_order.html'
    form_class = forms.CreateOrderForm

    def get_context_data(self, **kwargs):
        context = super(CreateOrderView, self).get_context_data()
        context['title'] = 'Добавление нового заказа'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.instance.price = form.instance.course.price
            order = form.save()
            payment = PaymentManager(order)
            payment.get_paid_uuid()
            payment.send_payment_url()
        return HttpResponseRedirect('/api/crm/orders')


class RequestListView(FilterMixin, ListView):
    """ Список онлайн заявок в CRM
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
        if self.request.user.staff.user_group == 'admin':
            queryset = Request.objects.filter(type_request='online').filter(is_deleted=False)
        elif self.request.user.staff.user_group == 'sale_manager':
            queryset = Request.objects.filter(
                Q(manager=self.request.user.staff) |
                Q(status='new')).filter(type_request='online').filter(is_deleted=False)
        else:
            return None
        return self.check_request_data(request=self.request, queryset=queryset)

    @staticmethod
    def get_status():
        """ Получает статусы заявок для фильтрации """
        return Request.objects.all().values('status').distinct()


class OutCallListView(RequestListView):
    """ Список исходящих звонков в CRM
    """
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OutCallListView, self).get_context_data(**kwargs)
        context['title'] = 'Исходящие звонки'
        return context

    def get_queryset(self):
        if self.request.user.staff.user_group == 'admin':
            queryset = Request.objects.filter(type_request='outgoing_call').filter(is_deleted=False)
        elif self.request.user.staff.user_group == 'sale_manager':
            queryset = Request.objects.filter(
                manager=self.request.user.staff).filter(type_request='outgoing_call').filter(is_deleted=False)
        else:
            return None
        return self.check_request_data(request=self.request, queryset=queryset)


class InCallListView(RequestListView):
    """ Список входящих звонков в CRM
    """
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InCallListView, self).get_context_data(**kwargs)
        context['title'] = 'Входящие звонки'
        return context

    def get_queryset(self):
        if self.request.user.staff.user_group == 'admin':
            queryset = Request.objects.filter(type_request='incoming_call').filter(is_deleted=False)
        elif self.request.user.staff.user_group == 'sale_manager':
            queryset = Request.objects.filter(
                manager=self.request.user.staff).filter(type_request='incoming_call').filter(is_deleted=False)
        else:
            return None
        return self.check_request_data(request=self.request, queryset=queryset)


class VisitListView(RequestListView):
    """ Список визитов в CRM
    """
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VisitListView, self).get_context_data(**kwargs)
        context['title'] = 'Визиты'
        return context

    def get_queryset(self):
        if self.request.user.staff.user_group == 'admin':
            queryset = Request.objects.filter(type_request='visit').filter(is_deleted=False)
        elif self.request.user.staff.user_group == 'sale_manager':
            queryset = Request.objects.filter(
                manager=self.request.user.staff).filter(type_request='visit').filter(is_deleted=False)
        else:
            return None
        return self.check_request_data(request=self.request, queryset=queryset)


class DeletedRequestListView(RequestListView):
    """ Список удаленных заявок в CRM
    """
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeletedRequestListView, self).get_context_data(**kwargs)
        context['title'] = 'Заявки - Корзина'
        return context

    def get_queryset(self):
        if self.request.user.staff.user_group == 'admin':
            queryset = Request.objects.filter(is_deleted=True)
        elif self.request.user.staff.user_group == 'sale_manager':
            queryset = Request.objects.filter(manager=self.request.user.staff).filter(is_deleted=True)
        else:
            return None
        return self.check_request_data(request=self.request, queryset=queryset)


class RequestDetailView(DetailView):
    """ Детальное представление онлайн заявки в CRM
    """
    model = Request
    template_name = 'crm/request_detail.html'
    context_object_name = 'request'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RequestDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        redirect_url_dict = {
            'incoming_call': 'in-calls',
            'outgoing_call': 'out-calls',
            'online': 'online-requests',
            'visit': 'visits'
        }
        request = self.get_object()
        request.is_deleted = True if not request.is_deleted else False
        request.save()
        return HttpResponseRedirect(f'/api/crm/{redirect_url_dict.get(request.type_request)}')


class CreateRequestView(CreateView):
    """ Регистрация новой заявки в CRM
    """
    template_name = 'crm/create_request.html'
    form_class = forms.CreateRequestForm
    success_urls = {
        'incoming_call': '/api/crm/in-calls',
        'outgoing_call': '/api/crm/out-calls/',
        'online': '/api/crm/online-requests',
        'visit': '/api/crm/visits'
    }

    def get_context_data(self, **kwargs):
        context = super(CreateRequestView, self).get_context_data()
        context['title'] = 'Добавление новой заявки'
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_request = form.save()
            new_request.manager = self.request.user.staff
            new_request.save()
            new_request.client.last_status = new_request.result
            new_request.client.save()
            return HttpResponseRedirect(self.success_urls[form.instance.type_request])


class UpdateRequestView(UpdateView):
    """ Редактирование заявки в CRM
    """
    model = Request
    template_name = 'crm/update_request.html'
    form_class = forms.UpdateRequestForm
    context_object_name = 'request'

    def get_context_data(self, **kwargs):
        context = super(UpdateRequestView, self).get_context_data()
        context['title'] = 'Редактирование заявки'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            form.instance.manager = self.request.user.staff
            form.instance.save()
            return HttpResponseRedirect(f'/api/crm/requests/{self.get_object().pk}')


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
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'hr':
            return Vacancy.objects.all()
        else:
            return None


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


class CreateVacancyView(CreateView):
    """ Регистрация новой вакансии в CRM
    """
    template_name = 'crm/create_vacancy.html'
    form_class = forms.VacancyForm

    def get_context_data(self, **kwargs):
        context = super(CreateVacancyView, self).get_context_data()
        context['title'] = 'Добавление новой вакансии'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/api/crm/vacancy')


class UpdateVacancyView(UpdateView):
    """ Редактирование вакансии в CRM
    """
    model = Vacancy
    template_name = 'crm/update_vacancy.html'
    form_class = forms.VacancyForm
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super(UpdateVacancyView, self).get_context_data()
        context['title'] = 'Редактирование вакансии'
        return context

    def get_success_url(self):
        return f'/api/crm/vacancy/{self.get_object().pk}'


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
        if self.request.user.staff.user_group == 'admin':
            return Interview.objects.all()
        elif self.request.user.staff.user_group == 'hr':
            return Interview.objects.filter(manager=self.request.user.staff)
        else:
            return None


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


class CreateInterviewView(CreateView):
    """ Регистрация новго собеседования в CRM
    """
    template_name = 'crm/create_interview.html'
    form_class = forms.CreateInterviewForm

    def get_context_data(self, **kwargs):
        context = super(CreateInterviewView, self).get_context_data()
        context['title'] = 'Добавление нового собеседования'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            form.instance.manager = self.request.user.staff
            form.instance.save()
        return HttpResponseRedirect('/api/crm/interview')


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
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'education_manager':
            return Course.objects.all()
        else:
            return None


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


class LessonDetailView(DetailView):
    """ Детальное представление урока в CRM
    """
    model = Lesson
    template_name = 'crm/lesson_detail.html'
    context_object_name = 'lesson'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class CreateCourseView(CreateView, CourseMixin):
    """ Регистрация новго курса в CRM
    """
    template_name = 'crm/create_course.html'
    form_class = forms.CourseForm

    def get_context_data(self, **kwargs):
        context = super(CreateCourseView, self).get_context_data()
        context['title'] = 'Добавление нового курса'
        context['teachers'] = Teacher.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            course = form.save()
            self.update_teachers(course, self.request)
        return HttpResponseRedirect('/api/crm/courses')


class UpdateCourseView(UpdateView, CourseMixin):
    """ Редактирование курса в CRM
    """
    model = Course
    template_name = 'crm/update_course.html'
    form_class = forms.CourseForm
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(UpdateCourseView, self).get_context_data()
        context['title'] = 'Редактирование курса'
        context['teachers'] = Teacher.objects.all()
        return context

    def get_success_url(self):
        return f'/api/crm/courses/{self.get_object().pk}'

    def form_valid(self, form):
        if form.is_valid():
            course = form.save()
            self.update_teachers(course, self.request)
            return HttpResponseRedirect(f'/api/crm/courses/{self.get_object().pk}')


class CreateLessonView(CreateView):
    """ Регистрация новго урока в CRM
    """
    template_name = 'crm/create_lesson.html'
    form_class = forms.LessonForm

    def get_context_data(self, **kwargs):
        context = super(CreateLessonView, self).get_context_data()
        context['title'] = 'Добавление нового урока'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/api/crm/courses')


class UpdateLessonView(UpdateView):
    """ Редактирование урока в CRM
    """
    model = Lesson
    template_name = 'crm/update_lesson.html'
    form_class = forms.LessonForm
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super(UpdateLessonView, self).get_context_data()
        context['title'] = 'Редактирование урока'
        return context

    def get_success_url(self):
        return f'/api/crm/courses/lessons/{self.get_object().pk}'


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
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'education_manager':
            return Timetable.objects.all()
        else:
            return None


class TimeTableDetailView(DetailView):
    """ Детальное представление записи рассписания в CRM
    """
    model = Timetable
    template_name = 'crm/timetable_detail.html'
    context_object_name = 'timetable'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TimeTableDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class CreateTimeTableView(CreateView):
    """ Регистрация новой записи в рассписание в CRM
    """
    template_name = 'crm/create_timetable.html'
    form_class = forms.TimeTableForm

    def get_context_data(self, **kwargs):
        context = super(CreateTimeTableView, self).get_context_data()
        context['title'] = 'Добавление новой записи в рассписание'
        return context

    def form_valid(self, form):
        days_of_week_list = self.request.POST.getlist('day_of_week')

        if not days_of_week_list and form.is_valid():
            form.save()
        else:
            date = form.cleaned_data.get('date')
            lesson = form.cleaned_data.get('lesson')
            group = form.cleaned_data.get('group')
            end_date = datetime.strptime(self.request.POST.get('end_date'), "%Y-%m-%d")

            while date.timestamp() <= end_date.timestamp():
                if str(date.strftime("%A")).lower() in days_of_week_list:
                    new_timetable = Timetable()
                    new_timetable.date = date
                    new_timetable.lesson = lesson
                    new_timetable.group = group
                    new_timetable.save()

                date += timedelta(days=1)

        return HttpResponseRedirect('/api/crm/timetable')


class UpdateTimeTableView(UpdateView):
    """ Редактирование записи рассписания в CRM
    """
    model = Timetable
    template_name = 'crm/update_timetable.html'
    form_class = forms.TimeTableForm
    context_object_name = 'timetable'

    def get_context_data(self, **kwargs):
        context = super(UpdateTimeTableView, self).get_context_data()
        context['title'] = 'Редактирование рассписания'
        return context

    def get_success_url(self):
        return f'/api/crm/timetable/{self.get_object().pk}'


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
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'education_manager':
            return AcademicPerformance.objects.all()
        else:
            return None


class CreateAcademicPerformanceView(CreateView):
    """ Регистрация новой оценки в системе успеваемости в CRM в CRM
    """
    template_name = 'crm/create_academic_performance.html'
    form_class = forms.CreateAcademicPerformanceForm

    def get_context_data(self, **kwargs):
        context = super(CreateAcademicPerformanceView, self).get_context_data()
        context['title'] = 'Добавление новой оценки'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/api/crm/academic-performance')


class TeacherListView(ListView):
    """ Список преподавателей в CRM
    """
    model = Teacher
    template_name = 'crm/teacher_list.html'
    context_object_name = 'teacher_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['title'] = 'Преподаватели'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'education_manager' \
                or self.request.user.staff.user_group == 'hr':
            return Teacher.objects.all()
        else:
            return None


class TeacherDetailView(DetailView):
    """ Детальное представление преподавателя в CRM
    """
    model = Teacher
    template_name = 'crm/teacher_detail.html'
    context_object_name = 'teacher'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeacherDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class CreateTeacherView(FormView):
    """ Регистрация новго преподавателя в CRM
    """
    template_name = 'crm/create_teacher.html'
    form_class = forms.CreateTeacherForm

    def get_context_data(self, **kwargs):
        context = super(CreateTeacherView, self).get_context_data()
        context['title'] = 'Регистрация нового преподавателя'
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Teacher.objects.create(
                user=new_user,
                middle_name=form.cleaned_data['middle_name'],
                phone=form.cleaned_data['phone'],
                gender=form.cleaned_data['gender'],
                user_group='teacher'
            )
        return HttpResponseRedirect('/api/crm/teachers')


class UpdateTeacherView(UpdateView, TeacherMixin):
    """ Редактирование преподавателя в CRM
    """
    model = Teacher
    template_name = 'crm/update_teacher.html'
    form_class = forms.UpdateTeacherForm
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super(UpdateTeacherView, self).get_context_data()
        context['teacher'] = self.get_object()
        context['title'] = 'Редактирование преподавателя'
        context['group_list'] = Group.objects.all()
        context['course_list'] = Course.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            teacher = self.get_object()
            self.update_teacher_groups(teacher, self.request)
            self.update_teacher_courses(teacher, self.request)
            return HttpResponseRedirect(f'/api/crm/teachers/{teacher.pk}')
        return HttpResponseRedirect(f'/api/crm/teachers')


class StudentListView(ListView):
    """ Список студентов в CRM
    """
    model = Student
    template_name = 'crm/student_list.html'
    context_object_name = 'student_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['title'] = 'Студенты'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'education_manager' \
                or self.request.user.staff.user_group == 'hr':
            return Student.objects.all()
        else:
            return None


class StudentDetailView(DetailView):
    """ Детальное представление студента в CRM
    """
    model = Student
    template_name = 'crm/student_detail.html'
    context_object_name = 'student'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class CreateStudentView(FormView):
    """ Регистрация новго студента в CRM
    """
    template_name = 'crm/create_student.html'
    form_class = forms.CreateTeacherForm

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data()
        context['title'] = 'Регистрация нового студента'
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Student.objects.create(
                user=new_user,
                middle_name=form.cleaned_data['middle_name'],
                phone=form.cleaned_data['phone'],
                gender=form.cleaned_data['gender'],
                user_group='student'
            )
        return HttpResponseRedirect('/api/crm/students')


class StaffListView(ListView):
    """ Список сотрудников в CRM
    """
    model = Staff
    template_name = 'crm/staff_list.html'
    context_object_name = 'staff_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        context['title'] = 'Сотрудники'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.staff.user_group == 'admin' or self.request.user.staff.user_group == 'hr':
            return Staff.objects.all()
        else:
            return None


class StaffDetailView(DetailView):
    """ Детальное представление сотрудника в CRM
    """
    model = Staff
    template_name = 'crm/staff_detail.html'
    context_object_name = 'staff'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StaffDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        if self.get_object().user_group == 'sale_manager':
            context['client_list'] = Client.objects.filter(manager=self.get_object())
            context['request_list'] = Request.objects.filter(manager=self.get_object())
        elif self.get_object().user_group == 'education_manager':
            context['group_list'] = Group.objects.filter(manager=self.get_object())
        elif self.get_object().user_group == 'hr':
            context['interview_list'] = Interview.objects.filter(manager=self.get_object())
        return context


class CreateStaffView(FormView):
    """ Регистрация новго сотрудника в CRM
    """
    template_name = 'crm/create_staff.html'
    form_class = forms.CreateStaffForm

    def get_context_data(self, **kwargs):
        context = super(CreateStaffView, self).get_context_data()
        context['title'] = 'Регистрация нового сотрудника'
        return context

    def form_valid(self, form):
        if form.is_valid():
            if form.is_valid():
                new_user = User.objects.create(
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    is_staff=True
                )
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                Staff.objects.create(
                    user=new_user,
                    middle_name=form.cleaned_data['middle_name'],
                    phone=form.cleaned_data['phone'],
                    gender=form.cleaned_data['gender'],
                    user_group=form.cleaned_data['user_group']
                )
        return HttpResponseRedirect('/api/crm/staffs')


class GroupListView(ListView):
    """ Список учебных групп в CRM
    """
    model = Group
    template_name = 'crm/group_list.html'
    context_object_name = 'group_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['title'] = 'Группы'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Group.objects.all() if self.request.user.is_staff else None


class GroupDetailView(DetailView):
    """ Детальное представление учебной группы  в CRM
    """
    model = Group
    template_name = 'crm/group_detail.html'
    context_object_name = 'group'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        context['student_list'] = self.get_object().student_groups.all()
        return context


class CreateGroupView(CreateView, GroupMixin):
    """ Создание новой учебной группы в CRM
    """
    template_name = 'crm/create_group.html'
    form_class = forms.GroupForm

    def get_context_data(self, **kwargs):
        context = super(CreateGroupView, self).get_context_data()
        context['title'] = 'Добавление новой группы'
        context['student_list'] = Student.objects.all()
        context['course_list'] = Course.objects.all()
        context['teacher_list'] = Teacher.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_group = form.save()
            new_group.manager = self.request.user.staff
            courses_id_list = self.request.POST.getlist('courses')
            for course_id in courses_id_list:
                try:
                    course = Course.objects.get(pk=int(course_id))
                    new_group.courses.add(course)
                except Course.DoesNotExist:
                    continue
            new_group.save()
            self.update_students_group(new_group, self.request)
            self.update_teachers_group(new_group, self.request)
        return HttpResponseRedirect('/api/crm/groups')


class UpdateGroupView(UpdateView, GroupMixin):
    """ Редактирование группы в CRM
    """
    model = Group
    template_name = 'crm/update_group.html'
    form_class = forms.GroupForm
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super(UpdateGroupView, self).get_context_data()
        context['title'] = 'Редактирование группы'
        context['student_list'] = Student.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            group = form.save()
            self.update_students_group(group, self.request)
            return HttpResponseRedirect(f'/api/crm/groups/{self.get_object().pk}')


class CostCategoryListView(ListView):
    """ Список категорий затрат в CRM
    """
    model = CostCategory
    template_name = 'crm/cost_categories_list.html'
    context_object_name = 'category_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CostCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Категории затрат'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return CostCategory.objects.all() if self.request.user.is_staff else None


class CostCategoryDetailView(DetailView):
    """ Детальное представление категории затрат в CRM
    """
    model = CostCategory
    template_name = 'crm/cost_categories_detail.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CostCategoryDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        context['cost_list'] = Cost.objects.filter(category=self.get_object())
        return context


class CreateCostCategoryView(CreateView):
    """ Добавление новой категории затрат в CRM
    """
    template_name = 'crm/create_cost_category.html'
    form_class = forms.CostCategoryForm

    def get_context_data(self, **kwargs):
        context = super(CreateCostCategoryView, self).get_context_data()
        context['title'] = 'Добавление новой категории затрат'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/api/crm/cost-categories')


class UpdateCostCategoryView(UpdateView):
    """ Редактирование категории затрат в CRM
    """
    model = CostCategory
    template_name = 'crm/update_cost_category.html'
    form_class = forms.CostCategoryForm
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(UpdateCostCategoryView, self).get_context_data()
        context['title'] = 'Редактирование категории затрат'
        return context

    def get_success_url(self):
        return f'/api/crm/cost-categories/{self.get_object().pk}'


class CostListView(ListView):
    """ Список категорий затрат в CRM
    """
    model = Cost
    template_name = 'crm/cost_list.html'
    context_object_name = 'cost_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CostListView, self).get_context_data(**kwargs)
        context['title'] = 'Категории затрат'
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return Cost.objects.all() if self.request.user.is_staff else None


class CostDetailView(DetailView):
    """ Детальное представление затрат в CRM
    """
    model = Cost
    template_name = 'crm/cost_detail.html'
    context_object_name = 'cost'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CostDetailView, self).get_context_data(**kwargs)
        context['title'] = self.get_object()
        context['user'] = self.request.user
        return context


class CreateCostView(CreateView):
    """ Добавление затрат в CRM
    """
    template_name = 'crm/create_cost.html'
    form_class = forms.CostForm

    def get_context_data(self, **kwargs):
        context = super(CreateCostView, self).get_context_data()
        context['title'] = 'Добавление затрат'
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_cost = form.save()
            new_cost.user = self.request.user
            new_cost.save()
        return HttpResponseRedirect('/api/crm/costs')


class UpdateCostView(UpdateView):
    """ Редактирование затрат в CRM
    """
    model = Cost
    template_name = 'crm/update_cost.html'
    form_class = forms.CostForm
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(UpdateCostView, self).get_context_data()
        context['title'] = 'Редактирование затрат'
        return context

    def get_success_url(self):
        return f'/api/crm/costs/{self.get_object().pk}'
