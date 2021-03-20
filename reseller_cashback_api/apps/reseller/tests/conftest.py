import pytest
from django.contrib.auth.models import User
from model_bakery import baker

from ..models import Reseller

pytestmark = pytest.mark.django_db


@pytest.fixture
def reseller_data():
    return {
        'name': 'John Smith',
        'cpf': '123.456.789-90',
    }


@pytest.fixture
def user_data():
    return {
        'email': 'test@a.com',
        'passowrd': 'secure_password',
    }


@pytest.fixture
def user():
    return baker.make(User)


@pytest.fixture
def reseller(user):
    return baker.make(Reseller, user=user)
