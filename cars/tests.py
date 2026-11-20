from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Car, Owner
from .views import CarViewSet


# UNIT TEST: 
class CarControllerUnitTest(TestCase):
    def test_controller_initialization(self):
        """Аналог contextLoads() / assertThat(controller).isNotNull()"""
        viewset = CarViewSet()
        self.assertIsNotNone(viewset)


# INTEGRATION TEST: тестируем работу базой данных
class OwnerRepositoryTest(TestCase):
    def test_save_owner(self):
        """Аналог saveOwner(): создание и поиск объекта"""
        owner = Owner.objects.create(first_name="Aiman", last_name="Oral")
        found_owner = Owner.objects.filter(first_name="Aiman").first()

        self.assertIsNotNone(found_owner)
        self.assertEqual(found_owner.last_name, "Oral")

    def test_delete_owners(self):
        """Аналог deleteOwners(): создание и полное удаление"""
        Owner.objects.create(first_name="Lisa", last_name="Morrison")
        Owner.objects.all().delete()

        self.assertEqual(Owner.objects.count(), 0)


#Тестирование JWT авторизации через REST API
class CarRestTest(APITestCase):

    def setUp(self):
        self.username = 'admin'
        self.password = 'admin'
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

    def test_authentication(self):
        login_url = '/login'
        payload = {'username': self.username, 'password': self.password}

        response = self.client.post(login_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
