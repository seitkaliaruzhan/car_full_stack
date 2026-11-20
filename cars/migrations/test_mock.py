from unittest.mock import patch
import requests
from django.test import TestCase


# Тест үшін қолданылатын сыртқы сұраныс жасайтын функция
def get_external_car_info():
  response = requests.get('https://api.example.com/cars/status')
  return response.json()


class ExternalApiMockTest(TestCase):

  @patch('requests.get')
  def test_external_api_mock(self, mock_get):
    """Мок-тест: сыртқы API-ден келетін HTTP-сұранысты имитациялау"""
    #интернетке бармай, жасанды жауап қайтару
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'status': 'active',
        'car': 'Toyota Camry',
    }

    # Функцияны іске қосамыз
    result = get_external_car_info()

    self.assertEqual(result['status'], 'active')
    self.assertEqual(result['car'], 'Toyota Camry')