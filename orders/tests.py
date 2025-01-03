from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MyOrderViewTest(TestCase):

    def test_not_logged_user_should_redirect(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/usuarios/login/?next=/pedidos/mi-orden/")

    def test_not_logged_user_should_redirect(self):
        url = reverse("my_order")
        user = get_user_model().objects.create(username="test")  # crear un usuario
        self.client.force_login(user)  # logear el usuario
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
