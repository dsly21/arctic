from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from django.urls import reverse_lazy

from .forms import CreationForm, FindFriendForm
from .models import UserFriendInstance


def find_friend_view(request):
    request_user = request.user
    # из всех друзей возвращаем ближайшего по возрасту, смотрим, чтобы он не был в списке друзей.
    # создаём инстанс User Friends, либо меняем если уже есть. Добавляем туда нового друга и обновляем дату
    # не должен получать сам себя
    # if UserFriendInstance.objects.exists(): # есть ли кто-то вообще
    #     if UserFriendInstance.objects.filter(user=request_user.id).exists()): # искал ли пользователь друзей раньше
    #         if UserFriendInstance.objects.get(user=request_user).date_action_use.hour < 24: # сколько прошло времени с последнего поиска
    #             error_message = 'слишком частое использование, вернитесь позже'
    #     else:
    #         UserFriendInstance.objects.create(user=request_user, )
    #     friend = UserFriendInstance.objects.filter(user_friends__not_in=request_user.id).first()
    # else:
    #     error_message = 'Друзей не нашлось'
    context = {}

    return render(request, 'users/find_friend.html', context)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class CustomPasswordChangeView(PasswordChangeView):
    success_url = 'users/password_change_done.html'


class FindFriendView(View):
    form_class = FindFriendForm
    initial = {'key': 'value'}
    template_name = 'users/find_friend.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # из всех друзей возвращаем ближайшего по возрасту, смотрим, чтобы он не был в списке друзей.
            # создаём инстанс User Friends, либо меняем если уже есть. Добавляем туда нового друга и обновляем дату
            # не должен получать сам себя
            if UserFriendInstance.objects.exists():  # есть ли кто-то вообще
                if UserFriendInstance.objects.filter(user=request.user.id).exists():  # искал ли пользователь друзей раньше
                    # TODO: add time validation
                    # TODO: add english comments
                    # TODO: add logic nearest to age
                    # if UserFriendInstance.objects.get(user=request.user).date_action_use.hour < 24:  # сколько прошло времени с последнего поиска
                    #     error_message = 'слишком частое использование, вернитесь позже'
                    # else:
                    # Возвращаем друга, но не самого себя
                    # Возвращаем друга, которого нет в списке друзей пользователя
                    friend = UserFriendInstance.objects\
                        .filter(user__not=request.user.id)\
                        .filter(user_friends__not_in=UserFriendInstance.objects
                                .get(user=request.user).user_friends)\
                        .first()
                    HttpResponse('')
                else:
                    friend = UserFriendInstance.objects.first()
                    UserFriendInstance.objects.create(
                        user=request.user,
                        social_network_nickname=request.POST.get('social_network_nickname'),
                        postal_address=request.POST.get('postal_address'),
                        user_friends=request.user.id
                    )

                    HttpResponse('')
            else:
                error_message = 'Друзей не нашлось'
        return render(request, self.template_name, {'form': form})


