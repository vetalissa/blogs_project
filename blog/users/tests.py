from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from users.forms import UserRegisterForm, UserLoginForm
from users.models import User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'testuser',
            'last_name': 'testuser',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        self.path = reverse('users:register')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertIsInstance(response.context['form'], UserRegisterForm)
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


class UserLoginViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.login_url = reverse('users:login')

    def test_user_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Авторизация')
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIsInstance(response.context['form'], UserLoginForm)

    def test_user_login_post_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, reverse('home'))

    def test_user_login_post_error(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }

        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response,
                            'Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.',
                            html=True)
