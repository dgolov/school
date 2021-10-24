from django.urls import path

from management.views import MainView, ProfileLoginView


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('auth/', ProfileLoginView.as_view(), name='auth'),
]
