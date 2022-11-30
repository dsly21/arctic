from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from django.urls import reverse_lazy

from .forms import UserCreateOrUpdateForm, FindFriendForm
from .models import UserFriendInstance


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
            if UserFriendInstance.objects.exists():
                '''
                Request user already looking for friends?
                '''
                request_user_friend_instance = UserFriendInstance.objects.filter(user=request.user)
                if request_user_friend_instance.exists():
                    # TODO: add logic nearest to age
                    # TODO: add display hours, then user will can use to action
                    date_action_use = request_user_friend_instance.first().date_action_use
                    if date_action_use < date_action_use + timedelta(days=1):
                        messages.error(
                            request,
                            'слишком частое использование, вернитесь позже.'
                            #f'{(date_action_use + timedelta(days=1)) - date_action_use} часов'
                        )
                        return render(request, self.template_name, {'form': form})
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
                        return render(request, self.template_name, {'form': form})

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
                messages.error(request, 'Друзей не нашлось(')
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})

