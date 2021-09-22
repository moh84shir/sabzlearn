from django.urls import path
from . import views


urlpatterns = [
    path('accounts/login', views.LoginView.as_view()),
    path('accounts/register', views.RegisterView.as_view()),
    path('accounts/logout', views.LogOut.as_view()),
]
