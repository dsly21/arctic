import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from users.models import UserFriendInstance

User = get_user_model()


YEAR_CHOICES = [(str(i), i) for i in range(1990, (datetime.datetime.today().year-4))]


class UserCreateForm(UserCreationForm):
    arctic_region_flag = forms.ChoiceField(
        choices=User.UserRegion.choices,
        label='Я из арктического региона',
        help_text='Выберете, если вы живёте в одном из регионов арктической зоны России (Список регионов)'
    )
    birth_year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        label='Ваша дата рождения',
        help_text='Укажите вашу настоящую дату рождения, это важно'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'birth_year',
            'arctic_region_flag',
        )


class AuthenticationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class FindFriendForm(forms.ModelForm):
    class Meta:
        model = UserFriendInstance
        fields = [
            'recipient_full_name',
            'postal_address',
            'zip_code',
            'social_network_nickname',
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'birth_year',
            'arctic_region_flag',
        ]
