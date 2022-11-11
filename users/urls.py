from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    )
from django.urls import path

from . import views
from .views import CustomPasswordChangeDoneView, CustomPasswordChangeView

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'password_change/',
        CustomPasswordChangeView.as_view(template_name='users/password_change_form.html'),
        name='password_change'
    ),
    path(
        'password_change/done/',
        CustomPasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
]