import pytest
from django.contrib.messages import get_messages
from django.test import Client, TestCase
from django.urls import reverse

from users.models import User, UserFriendInstance


@pytest.mark.django_db
class TestUserFindFriends(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='user1',
            # first_name='имя',
            # last_name='Фамилия',
            email='test@mail.ru',
            arctic_region_flag=True,
            birth_year=2000
        )
        self.user_2 = User.objects.create(
            username='user2',
            # first_name='имя',
            # last_name='Фамилия',
            email='test2@mail.ru',
            arctic_region_flag=False,
            birth_year=2000
        )
        self.client = Client()

        self.find_friend_data = {
            'recipient_full_name': 'test_username',
            'postal_address': 'test_address',
            'zip_code': '123456'
        }

    def test_anonymous_user_cant_find_friend(self):
        # GET
        response = self.client.get(reverse('find_friend'))
        self.assertEqual(response.status_code, 302)

        # POST
        response = self.client.post(reverse('find_friend'))
        self.assertEqual(response.status_code, 302)

        self.client.force_login(self.user)
        response = self.client.get(reverse('find_friend'))
        self.assertEqual(response.status_code, 200)

    def test_if_base_not_contains_friends_user_will_get_0_friends(self):
        self.client.force_login(self.user)
        self.assertEqual(UserFriendInstance.objects.exists(), False)

        response = self.client.post(reverse('find_friend'), self.find_friend_data)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertEqual(response.status_code, 200)
        self.assertIn('Друзей не нашлось(', messages)

    def test_response_data_user_find_friend(self):
        self.client.force_login(self.user)
        user_2_friend = UserFriendInstance.objects.create(
            user=self.user_2, **self.find_friend_data
        )

        response_with_friend = self.client.post(reverse('find_friend'), self.find_friend_data)
        content = response_with_friend.content.decode()

        self.assertEqual(response_with_friend.status_code, 200)
        self.assertIn(user_2_friend.recipient_full_name, content)
        self.assertIn(user_2_friend.postal_address, content)
        self.assertIn(user_2_friend.zip_code, content)
        # only one friend
        self.assertEqual(1, len(response_with_friend.context.dicts[3]))
        self.assertEqual(True, UserFriendInstance.objects.filter(user=self.user_2).exists())





