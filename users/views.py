from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from django.urls import reverse_lazy, reverse

from .forms import CreationForm, FindFriendForm
from .models import UserFriendInstance


def find_friend_result_view(request, obj):
    context = {
        'friend': obj,
    }
    return render(request, 'users/find_friend_modal.html', context)


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
                        .exclude(user=request.user)\
                        .exclude(user_friends=UserFriendInstance.objects
                                .get(user=request.user).user_friends)\
                        .first()
                    return render(request, "users/find_friend_modal.html", context={'friend': friend})
                    # return HttpResponseRedirect(reverse('find_friend_modal', args=(friend,)))
                else:
                    friend = UserFriendInstance.objects.first()
                    UserFriendInstance.objects.create(
                        user=request.user,
                        social_network_nickname=request.POST.get('social_network_nickname'),
                        postal_address=request.POST.get('postal_address'),
                        user_friends=request.user.id
                    )

                    return render(request, "users/find_friend_modal.html", context={'friend': friend})
            else:
                error_message = 'Друзей не нашлось'
        return render(request, self.template_name, {'form': form})

