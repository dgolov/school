from django.urls import path

from management import views


urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('auth/', views.ProfileLoginView.as_view(), name='auth'),
    path('clients/', views.ClientsListView.as_view(), name='clients'),
]
