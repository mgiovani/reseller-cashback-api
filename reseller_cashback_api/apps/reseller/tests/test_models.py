from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth.models import User
from model_bakery import baker

from ..models import Reseller


class ResellerModelTestCase(TestCase):

    def setUp(self):
        self.user = baker.make(User, username='user', email='test@a.com',
                               is_staff=False, is_superuser=False)

    def test_reseller_model_can_be_created(self):
        reseller = Reseller.objects.create(
            name='John Smith', cpf='123.456.789-90', user=self.user)
        self.assertTrue(isinstance(reseller, Reseller))
        self.assertEqual(reseller.name, 'John Smith')
        self.assertEqual(reseller.cpf, '123.456.789-90')

    def test_reseller_model_cannot_be_created_without_name(self):
        reseller = Reseller.objects.create(
            cpf='123.456.789-90', user=self.user)
        self.assertRaises(ValidationError, reseller.full_clean)

    def test_reseller_model_cannot_be_created_without_cpf(self):
        reseller = Reseller.objects.create(name='John Smith', user=self.user)
        self.assertRaises(ValidationError, reseller.full_clean)
