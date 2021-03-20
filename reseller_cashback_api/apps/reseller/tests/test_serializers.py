import pytest
from django.test import TestCase

from apps.reseller.serializers import ResellerSerializer


class ResellerSerializerTestCase(TestCase):

    def setUp(self):
        self.reseller_valid_data = {
            'name': 'John Smith',
            'cpf': '123.456.789-90',
            'user': {
                'email': 'test@a.com',
                'password': 'secure_password',
            }
        }
        self.reseller_invalid_data = {'any': 'thing'}

    def test_reseller_serializer_is_valid_with_all_fields(self):
        serializer = ResellerSerializer(data=self.reseller_valid_data)
        self.assertTrue(serializer.is_valid())

    def test_reseller_serializer_is_not_valid_without_required_fields(self):
        serializer = ResellerSerializer(data=self.reseller_invalid_data)
        self.assertFalse(serializer.is_valid())
