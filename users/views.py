from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from django.urls import reverse_lazy, reverse

from .forms import UserCreateOrUpdateForm, FindFriendForm
from .models import UserFriendInstance, User


@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UserCreateOrUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UserCreateOrUpdateForm(instance=request.user)
    return render(request, 'users/user_profile.html', {'user_form': user_form})


@login_required
def find_friend_result_view(request, obj):
    context = {
        'friend': obj,
    }
    return render(request, 'users/find_friend_modal.html', context)


class SignUp(CreateView):
    form_class = UserCreateOrUpdateForm
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
                '''
                Request user already looking for friends?
                '''
                if UserFriendInstance.objects.filter(user=request.user.id).exists():
                    # TODO: add time validation
                    # TODO: add english comments
                    # TODO: add logic nearest to age
                    # TODO: add logic not admin
                    # if UserFriendInstance.objects.get(user=request.user).date_action_use.hour < 24:  # сколько прошло времени с последнего поиска
                    #     error_message = 'слишком частое использование, вернитесь позже'
                    # else:
                    # Возвращаем друга, но не самого себя
                    # Возвращаем друга, которого нет в списке друзей пользователя
                    '''
                    Return a friend but not:
                     - himself
                     - admin
                     - not a user who has already been
                    '''
                    friend = UserFriendInstance.objects\
                        .exclude(user=request.user)\
                        .exclude(user_friends=request.user)\
                        .first()

                    if friend:
                        friend.user_friends = request.user
                        friend.save()
                        return render(request, "users/find_friend_modal.html", context={'friend': friend})
                    else:
                        messages.error(request, 'Друзей не нашлось(')
                        # return render(request, "users/find_friend.html")

                else:
                    friend = UserFriendInstance.objects.first()
                    UserFriendInstance.objects.create(
                        user=request.user,
                        locality=request.POST.get('locality'),
                        recipient_full_name=request.POST.get('recipient_full_name'),
                        country_subject=request.POST.get('country_subject'),
                        zip_code=request.POST.get('zip_code'),
                        social_network_nickname=request.POST.get('social_network_nickname'),
                        postal_address=request.POST.get('postal_address'),
                    )
                    friend.user_friends = request.user
                    friend.save()
                    return render(request, "users/find_friend_modal.html", context={'friend': friend})
            else:
                error_message = 'Друзей не нашлось'
        return render(request, self.template_name, {'form': form})

