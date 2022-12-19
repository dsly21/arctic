from datetime import timedelta, datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from django.urls import reverse_lazy

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

    # @base_view
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # @base_view
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            if UserFriendInstance.objects.exists():
                '''
                Request user already looking for friends?
                '''
                request_user_friend_instance = UserFriendInstance.objects.filter(user=request.user).first()
                if request_user_friend_instance:
                    # TODO: add logic nearest to age
                    # TODO: add display hours, then user will can use to action
                    date_action_use = request_user_friend_instance.date_action_use
                    if (datetime.now() - date_action_use.replace(tzinfo=None)) < timedelta(days=1):
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
                    friend = (UserFriendInstance.objects
                        .exclude(user=request.user)                                             # himself
                        .exclude(user__is_superuser=True)                                       # admin
                        .exclude(user__username__in=request_user_friend_instance.user_friends)  # not a user who has
                                                                                                # already been
                        .exclude(user__arctic_region_flag=request.user.arctic_region_flag)      # user with same region
                        .order_by('friendship_count')
                        .first())

                    if friend:
                        request_user_friend_instance.date_action_use = datetime.now()
                        request_user_friend_instance.user_friends.append(friend.user.username)
                        request_user_friend_instance.save()

                        friend.friendship_count += 1
                        friend.save()

                        return render(request, "users/find_friend_modal.html", context={'friend': friend})
                    else:
                        messages.error(request, 'Друзей не нашлось(')
                        return render(request, self.template_name, {'form': form})

                else:
                    request_user_friend_instance = UserFriendInstance.objects.create(
                        user=request.user,
                        recipient_full_name=request.POST.get('recipient_full_name'),
                        zip_code=request.POST.get('zip_code'),
                        social_network_nickname=request.POST.get('social_network_nickname'),
                        postal_address=request.POST.get('postal_address'),
                    )

                    friend = (UserFriendInstance.objects
                        .exclude(user__is_superuser=True)
                        .exclude(user=request.user)
                        .exclude(user__arctic_region_flag=request.user.arctic_region_flag)
                        .order_by('friendship_count')
                        .first())

                    if friend:
                        request_user_friend_instance.user_friends.append(friend.user.username)
                        request_user_friend_instance.save()

                        friend.friendship_count += 1
                        friend.save()
                        return render(request, "users/find_friend_modal.html", context={'friend': friend})
                    else:
                        messages.error(request, 'Друзей не нашлось(')
                        return render(request, self.template_name, {'form': form})
            else:
                messages.error(request, 'Друзей не нашлось(')
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


def password_reset_view(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            mail = password_reset_form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=mail)
            except Exception:
                user = False
            if user:
                subject = 'Запрошено восстановление пароля'
                email_template = 'users/password_reset_msg.html'
                cont = {
                    'email': user.email,
                    'domain': 'arktikavkonverte.ru',
                    'site_name': '',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'https'
                }
                msg_html = render_to_string(email_template, cont)
                try:
                    send_mail(
                        subject,
                        'ссылка',
                        settings.EMAIL_HOST_USER,
                        [user.email],
                        fail_silently=True,
                        html_message=msg_html
                    )
                except BadHeaderError:
                    return HttpResponse('Обнаружен недопустимый заголовок.')
                return redirect('password_reset_done')
        else:
            messages.error(request, 'пользователь не найден, сообщите о проблеме администратору')
            return redirect('password_reset')

    password_reset_form = PasswordResetForm()
    return render(request, 'users/password_reset_form.html', {'form': password_reset_form})

