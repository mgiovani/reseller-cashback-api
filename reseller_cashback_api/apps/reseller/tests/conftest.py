import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from ..models import Reseller

pytestmark = pytest.mark.django_db


@pytest.fixture
def reseller_data():
    return {
        'name': 'John Smith',
        'cpf': '123.456.789-90',
        'email': 'test@a.com',
        'password': 'secure_password',
    }


@pytest.fixture
def reseller(user):
    return baker.make(Reseller, user=user)


@pytest.fixture
def api_client():
    return APIClient()
