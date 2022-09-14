from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from mainapp.models import (
    Course,
    Category,
    Lesson,
    Group,
    Timetable,
    AcademicPerformance,
    Student,
    StudentAgeGroup,
    Teacher
)
from management.models import (
    Client,
    Contract,
    Order,
    Request,
    Vacancy,
    Interview,
    Staff,
    Cost,
    CostCategory,
    AdvertisingActivityCategory,
    AdvertisingActivity
)


class AuthForm(forms.Form):
    """ Форма входа пользователя в CRM
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Логин, телефон или email...'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль...'}
        )
    )


class ClientForm(forms.ModelForm):
    """ Форма регистрации и обновления клиента в CRM
    """
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите фамилию клиента...'}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя клиента...'}
        )
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите отчество клиента...'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона клиента...'}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите email клиента...'}
        )
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите город клиента...'}
        )
    )
    passport = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите серию и номер паспорта клиента...'}
        )
    )
    passport_issued_by = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите кем выдан паспорт...'}
        )
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите адрес прописки клиента...'}
        )
    )

    class Meta:
        model = Client
        fields = (
            'first_name', 'last_name', 'middle_name', 'phone', 'email', 'city',
            'passport', 'passport_issued_by', 'address'
        )


class CreateContractForm(forms.ModelForm):
    """ Форма регистрации нового контракта в CRM
    """
    number = forms.CharField(
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
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Введите комментарий менеджера...'}
        )
    )

    class Meta:
        model = Contract
        fields = ('number', 'client', 'course', 'comment')


class CreateOrderForm(forms.ModelForm):
    """ Форма регистрации нового заказа в CRM
    """
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    # payed = forms.BooleanField(
    #     widget=forms.Select(
    #         choices=(('False', 'Нет'), ('True', 'Да')),
    #         attrs={'class': 'form-control'}
    #     )
    # )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Order
        fields = ('client', 'payed', 'course')


class CreateRequestForm(forms.ModelForm):
    """ Форма регистрации новой заявки в CRM
    """
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    type_request = forms.CharField(
        widget=forms.Select(
            choices=Request.TYPE_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    status = forms.CharField(
        widget=forms.Select(
            choices=Request.STATUS_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    purpose = forms.CharField(
        widget=forms.Select(
            choices=Request.PURPOSE_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    result = forms.CharField(
        widget=forms.Select(
            choices=Request.RESULT_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    remind = forms.DateField(
        required=False,
        widget=AdminDateWidget(
            attrs={'class': 'form-control', 'type': "date"}
        )
    )
    comment = forms.CharField(
        required=False,
        label='Комментарий',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Введите комментарий менеджера...'}
        )
    )

    class Meta:
        model = Request
        fields = ('client', 'type_request', 'status', 'course', 'purpose', 'result', 'remind', 'comment')


class UpdateRequestForm(forms.ModelForm):
    """ Форма редактирования заявки в CRM
    """
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    type_request = forms.CharField(
        widget=forms.Select(
            choices=Request.TYPE_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    status = forms.CharField(
        widget=forms.Select(
            choices=Request.STATUS_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    purpose = forms.CharField(
        widget=forms.Select(
            choices=Request.PURPOSE_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    result = forms.CharField(
        widget=forms.Select(
            choices=Request.RESULT_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    remind = forms.DateField(
        required=False,
        widget=AdminDateWidget(
            attrs={'class': 'form-control', 'type': "date"}
        )
    )
    comment = forms.CharField(
        required=False,
        label='Комментарий',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'value': "PUT"}
        )
    )
    loyalty = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'type': 'range', 'class': 'form-control'}
        )
    )

    class Meta:
        model = Request
        fields = ('type_request', 'status', 'course', 'purpose', 'loyalty', 'result', 'remind', 'comment')


class VacancyForm(forms.ModelForm):
    """ Форма регистрации и редактирования вакансии в CRN
    """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название вакансии...'}
        )
    )
    salary = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите зарплату...'}
        )
    )
    requirements = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
    conditions = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Vacancy
        fields = ('name', 'salary', 'requirements', 'conditions', 'comment')


class CreateInterviewForm(forms.ModelForm):
    """ Форма регистрации нового собеседования в CRM
    """
    vacancy = forms.ModelChoiceField(
        queryset=Vacancy.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите фамилию...'}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя...'}
        )
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите отчество...'}
        )
    )
    age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите возраст...'}
        )
    )
    place_of_study = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите место учебы...'}
        )
    )
    place_of_work = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите место работы...'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите номер телефона...'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите электронную почту...'}
        )
    )
    result = forms.CharField(
        widget=forms.Select(
            choices=Interview.RESULT_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    date = forms.DateField(
        required=False,
        widget=AdminDateWidget(
            attrs={'class': 'form-control', 'type': "date"}
        )
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Interview
        fields = (
            'vacancy', 'last_name', 'first_name', 'middle_name', 'age', 'place_of_study', 'place_of_work', 'phone',
            'email', 'result', 'date', 'comment'
        )


class CourseForm(forms.ModelForm):
    """ Форма регистрации и редактирования курса в CRM
    """
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название курса...'}
        )
    )
    price = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите цену курса...'}
        )
    )
    duration = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    education_type = forms.CharField(
        widget=forms.Select(
            choices=Course.TYPE_CHOICES,
            attrs={'class': 'form-control single-select select2-hidden-accessible'}
        )
    )
    color_hex = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    complexity = forms.CharField(
        widget=forms.Select(
            choices=Course.COMPLEXITY_CHOICES,
            attrs={'class': 'form-control single-select select2-hidden-accessible'}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Course
        fields = (
            'category', 'name', 'price', 'duration', 'education_type', 'description', 'poster', 'video_presentation',
            'complexity', 'color_hex'
        )


class LessonForm(forms.ModelForm):
    """ Форма добавления и редактирования урока в CRM
    """
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    theme = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите тему урока...'}
        )
    )
    lesson_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите номер урока в курсе...'}
        )
    )
    video_slug = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Вставьте ссылку на видео урока...'}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
    material_link = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Вставьте ссылку на материалы урока...'}
        )
    )

    class Meta:
        model = Lesson
        fields = ('course', 'theme', 'lesson_number', 'video_slug', 'description', 'material_link')


class TimeTableForm(forms.ModelForm):
    """ Форма регистрации и редактирования записи в рассписании в CRM
    """
    date = forms.DateTimeField(
        widget=AdminDateWidget(
            attrs={'class': 'form-control', 'type': "datetime-local"}
        )
    )
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    material_link = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Вставьте ссылку на материалы...'}
        )
    )

    class Meta:
        model = Timetable
        fields = ('date', 'group', 'material_link')


class CreateAcademicPerformanceForm(forms.ModelForm):
    """ Форма регистрации новой оценки в системе успеваемости в CRM
    """
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    teacher = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    lesson = forms.ModelChoiceField(
        queryset=Lesson.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    type_grade = forms.BooleanField(
        widget=forms.Select(
            choices=AcademicPerformance.TYPE_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
    grade = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = AcademicPerformance
        fields = ('student', 'teacher', 'lesson', 'type_grade', 'grade')


class CreateTeacherForm(forms.Form):
    """ Форма регистрации преподавателя в CRM
    """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Логин...'}
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль...'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите фамилию...'}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя...'}
        )
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите отчество...'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите номер телефона...'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите электронную почту...'}
        )
    )
    gender = forms.CharField(
        widget=forms.Select(
            choices=Teacher.GENDER_CHOICES,
            attrs={'class': 'form-control'}
        )
    )


class UpdateStudentForm(forms.ModelForm):
    """ Форма добавления групп и курсов студенту """
    verification = forms.BooleanField(required=False)

    is_active = forms.BooleanField(required=False)

    class Meta:
        model = Student
        fields = ('verification', 'is_active')


class UpdateTeacherForm(forms.ModelForm):
    """ Форма редактирования преподавателя """
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите отчество...'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите номер телефона...'}
        )
    )
    education = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите образование...'}
        )
    )
    professional_activity = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Укажите профессиональную деятельность...'}
        )
    )

    class Meta:
        model = Teacher
        fields = ('middle_name', 'phone', 'education', 'professional_activity')


class CreateStaffForm(CreateTeacherForm):
    """ Форма регистрации сотрудника в CRM
    """
    user_group = forms.CharField(
        widget=forms.Select(
            choices=Staff.USER_GROUP_CHOICES,
            attrs={'class': 'form-control'}
        )
    )


class GroupForm(forms.ModelForm):
    """ Форма добавления и редактирования учебной группы в CRM
    """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название курса...'}
        )
    )

    class Meta:
        model = Group
        fields = ('name', )


class CostCategoryForm(forms.ModelForm):
    """ Форма добавления и редактирования категорий затрат в CRM
    """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название категории...'}
        )
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Введите комментарий...'}
        )
    )

    class Meta:
        model = CostCategory
        fields = ('name', 'comment',)


class CostForm(forms.ModelForm):
    """ Форма добавления и редактирования затрат в CRM
    """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название затраты...'}
        )
    )
    category = forms.ModelChoiceField(
        queryset=CostCategory.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    advertising_activity = forms.ModelChoiceField(
        required=False,
        queryset=AdvertisingActivity.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    date_to = forms.DateField(
        widget=AdminDateWidget(
            attrs={'class': 'form-control', 'type': "date"}
        )
    )
    date_from = forms.DateField(
        widget=AdminDateWidget(
            attrs={'class': 'form-control', 'type': "date"}
        )
    )
    amount = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Введите комментарий...'}
        )
    )

    class Meta:
        model = Cost
        fields = ('name', 'category', 'advertising_activity', 'date_to', 'date_from', 'amount', 'comment',)


class AdvertisingActivityForm(forms.ModelForm):
    """ Форма добавления и редактирования рекламной активности в CRM
        """
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название категории...'}
        )
    )

    class Meta:
        model = CostCategory
        fields = ('name',)
