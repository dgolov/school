from django.contrib.auth import views
from django.urls import path

from management.views import (
    MainView,
    ProfileLoginView,
    ClientsListView,
    ClientDetailView,
    CreateClientView,
    ContractListView,
    ContractDetailView,
    VacancyListView,
    VacancyDetailView,
    InterviewListView,
    InterviewDetailView,
    OrderListView,
    OrderDetailView,
    RequestListView,
    RequestDetailView,
    CourseListView,
    CourseDetailView,
    TimeTableListView,
    AcademicPerformanceListView,
)


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('auth/', ProfileLoginView.as_view(), name='auth'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create', CreateClientView.as_view(), name='create_client'),
    path('requests/', RequestListView.as_view(), name='requests'),
    path('requests/<int:pk>/', RequestDetailView.as_view(), name='requests_detail'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contracts_detail'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='orders_detail'),
    path('vacancy/', VacancyListView.as_view(), name='vacancy'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('interview/', InterviewListView.as_view(), name='interview'),
    path('interview/<int:pk>/', InterviewDetailView.as_view(), name='interview_detail'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('academic-performance/', AcademicPerformanceListView.as_view(), name='academic_performance'),
    path('timetable/', TimeTableListView.as_view(), name='timetable'),
]
