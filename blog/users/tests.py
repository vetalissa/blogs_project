from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from users.forms import UserRegisterForm
from users.models import User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'alisa',
            'last_name': 'alisa',
            'username': 'alisa',
            'email': 'alisa@gmail.com',
            'password1': 'privet201101',
            'password2': 'privet201101',
        }
        self.path = reverse('users:register')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertEqual(list(response.context_data['form'].fields), list(UserRegisterForm().fields))
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        username = self.data['username']

        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
