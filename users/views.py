# users/views.py
# Импортируем CreateView, чтобы создать ему наследника
#from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm, AuthenticationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class LoginView(CreateView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/login.html'


class LogoutView(CreateView):
    pass