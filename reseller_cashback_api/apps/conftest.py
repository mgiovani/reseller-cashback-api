import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from .reseller.models import Reseller
from .order.models import Order

pytestmark = pytest.mark.django_db

@pytest.fixture
def order_data():
    return {
        'code': 'ABC-123',
        'price': '123.45',
        'date': '2021-03-20',
    }

@pytest.fixture
def reseller_data():
    return {
        'name': 'John Smith',
        'cpf': '123.456.789-90',
        'email': 'test@a.com',
        'password': 'secure_password',
    }


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def fixed_reseller(reseller_data):
    reseller = baker.make(Reseller, **reseller_data)
    reseller.set_password(reseller.password)
    reseller.save()
    return reseller

@pytest.fixture
def reseller():
    return baker.make(Reseller)


@pytest.fixture
def fixed_order(order_data, fixed_reseller):
    return baker.make(Order, **order_data, reseller=fixed_reseller)


@pytest.fixture
def order(reseller):
    return baker.make(Order, reseller=reseller)
