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
    InterviewListView,
    OrderListView,
    RequestListView
)


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('auth/', ProfileLoginView.as_view(), name='auth'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create', CreateClientView.as_view(), name='create_client'),
    path('requests/', RequestListView.as_view(), name='requests'),
    path('contracts/', ContractListView.as_view(), name='contracts'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contracts_detail'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('interview/', InterviewListView.as_view(), name='interview'),
]
