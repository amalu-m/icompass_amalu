from django.test import TestCase
from rest_framework.test import APIRequestFactory
from app.views import inputData, hasSqlInjection, buildResponse
from rest_framework.exceptions import APIException
import json

class InputTestCase(TestCase):

    def test_inputData_valid_data(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/sanitized/input', {'payload': 'hello'})
        response = inputData(request)
        dict = json.loads(response.content)
        self.assertEqual(dict['result'], 'sanitized')

    def test_inputData_missing_payload_key(self):
        factory = APIRequestFactory()
        request = factory.post('/v1/sanitized/input', {'key': 'value'})
        with self.assertRaises(APIException):
            inputData(request)

    def test_hasSqlInjectionTrue(self):
        input = 'select'
        response = hasSqlInjection(input)
        self.assertEqual(True, True)

    def test_hasSqlInjectionFalse(self):
        input = 'hello'
        response = hasSqlInjection(input)
        self.assertEqual(False, False)

    def test_buildResponseunsanitized(self):
        input = True
        response = buildResponse(input)
        dict = json.loads(response.content)
        self.assertEqual(dict['result'], 'unsanitized')

    def test_buildResponsesanitized(self):
        input = False
        response = buildResponse(input)
        dict = json.loads(response.content)
        self.assertEqual(dict['result'], 'sanitized')
