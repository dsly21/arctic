from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, reverse_lazy

from .views import (
    SignUp,
    password_reset_view,
    user_get_or_update,
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
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            success_url=reverse_lazy('users:password_change_done')
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    path(
        'user_profile/',
        user_get_or_update,
        name='user-profile'
    ),
    path(
        'password_reset/',
        password_reset_view,
        name='password_reset'
    ),
    path(
        'password_reset/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password_reset/complete/',
        PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    )
]
