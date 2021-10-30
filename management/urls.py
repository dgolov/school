from django.contrib.auth import views
from django.urls import path

from management.views import (
    MainView,
    ProfileLoginView,
    ClientsListView,
    ClientDetailView,
    CreateClientView,
    ContractListView,
    InterviewListView,
    OrderListView,
    RequestListView
)


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('auth/', ProfileLoginView.as_view(), name='auth'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('clients/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create', CreateClientView.as_view(), name='create_client'),
    path('requests/', RequestListView.as_view(), name='requests'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('interview/', InterviewListView.as_view(), name='interview'),
]
