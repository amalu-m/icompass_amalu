from django.test import TestCase
from rest_framework.test import APIRequestFactory
from app.views import inputData
import json

class InputTestCase(TestCase):
    def test_sanitized_inputData(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/sanitized/input', {'payload': 'hello'})
        response = inputData(request)
        dict = json.loads(response.content)
        self.assertEqual(dict['result'], 'sanitized')

    def test_unsanitized_inputData_lower_case(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/sanitized/input', {'payload': 'select'})
        response = inputData(request)
        dict = json.loads(response.content)
        self.assertEqual(dict['result'], 'unsanitized')

    def test_unsanitized_inputData_upper_case(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/sanitized/input', {'payload': 'DELETE'})
        response = inputData(request)
        dict = json.loads(response.content)
        self.assertEqual(dict['result'], 'unsanitized')
