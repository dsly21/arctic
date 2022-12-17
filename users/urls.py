from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
)
from django.urls import path

from .views import (
    CustomPasswordChangeDoneView,
    CustomPasswordChangeView,
    user_profile,
    SignUp, password_reset_view,
)

app_name = 'users'


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
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
    path(
        'user_profile/',
        user_profile,
        name='user-profile'
    ),
    path(
        'password_reset/',
        password_reset_view,
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'
    )
]
