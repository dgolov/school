from django.contrib.auth import views
from django.urls import path

from management.views import (
    MainView,
    ProfileLoginView,
    ClientsListView,
    ContractListView,
    InterviewListView
)


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('auth/', ProfileLoginView.as_view(), name='auth'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('contracts/', ContractListView.as_view(), name='requests'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('contracts/', ContractListView.as_view(), name='orders'),
    path('interview/', InterviewListView.as_view(), name='interview'),
]
