from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AdminLoginTests(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = 'adminpass'
        self.user = User.objects.create_superuser(username=self.username, email='admin@example.com', password=self.password)
        self.login_url = reverse('admin:login')

    def test_admin_login_page_loads(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ласкаво просимо до Oishii Admin')

    def test_admin_login_success(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertContains(response, 'Oishii Admin')


    def test_admin_login_failure(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Невірне ім’я користувача або пароль')
        self.assertFalse(response.context['user'].is_authenticated)
