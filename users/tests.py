import pytest
from django.test import Client, TestCase
from django.urls import reverse

from users.models import User, UserFriendInstance


@pytest.mark.django_db
class TestUserFindFriends(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Имя',
            last_name='Фамилия',
            email='test@mail.ru',
            arctic_region_flag=True,
            birth_year=2000
        )
        self.client = Client()

    def test_anonimous_user_cant_use_func(self):
        response = self.client.get(reverse('find_friend'))
        # self.assertRedirects(response, reverse('users:signup'))

        self.assertEqual(UserFriendInstance.objects.exists(), False)

        self.client.login()
        response = self.client.get(reverse('find_friend'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserFriendInstance.objects.exists(), True)



