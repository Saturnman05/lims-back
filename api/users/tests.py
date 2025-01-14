from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
            full_name="Test User",
            cedula="12345678901",
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_create_user(self):
        """Prueba la creación de un nuevo usuario."""
        url = reverse("user-list")  # Reemplaza 'user-list' con el nombre de tu URL
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
            "full_name": "New User",
            "cedula": "98765432101",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.data["username"], data["username"])

    def test_get_user_list(self):
        """Prueba la obtención de la lista de usuarios."""
        url = reverse("user-list")  # Reemplaza 'user-list' con el nombre de tu URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_detail(self):
        """Prueba la obtención de los detalles de un usuario."""
        url = reverse("user-detail")  # Reemplaza 'user-detail' con el nombre de tu URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"]["username"], self.user.username)

    def test_get_user_detail_unauthenticated(self):
        """Prueba la obtención de detalles de usuario sin autenticación."""
        self.client.credentials()  # Elimina las credenciales
        url = reverse("user-detail")  # Reemplaza 'user-detail' con el nombre de tu URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
