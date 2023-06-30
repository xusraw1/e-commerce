from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class SignUpTest(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('signup'),
            data={
                'first_name': 'xusraw',
                'username': 'scatr1x',
                'email': 'xusraw2003@gmail.com',
                'password1': 'Bitcoin2003',
                'password2': 'Bitcoin2003',
            }
        )
        user = CustomUser.objects.get(username='xusraw')
        self.assertEqual(user.firstname, 'xusraw')
        self.assertEqual(user.email, 'xusraw2003@gmail.com')
        self.assertTrue(user.chek_passwor('xusraw'))
