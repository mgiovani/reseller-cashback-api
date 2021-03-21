import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from ..models import Order, OrderStatus

pytestmark = pytest.mark.django_db


def test_order_model_can_be_created(order_data, reseller):
    order = Order.objects.create(**order_data, reseller=reseller)
    assert isinstance(order, Order)
    assert order.code == order_data['code']
    assert order.price == order_data['price']
    assert order.date == order_data['date']
    assert order.status == OrderStatus.VALIDATION.name


def test_order_model_can_be_created_pre_approved(order_data, fixed_reseller):
    order = Order.objects.create(**order_data, reseller=fixed_reseller)
    assert isinstance(order, Order)
    assert order.code == order_data['code']
    assert order.price == order_data['price']
    assert order.date == order_data['date']
    assert order.status == OrderStatus.APPROVED.name


@pytest.mark.parametrize("required_field", ['code', 'price', 'date'])
def test_order_model_cannot_be_created_without_required_fields(
        order_data, required_field, reseller):

    del order_data[required_field]
    with pytest.raises((ValidationError, IntegrityError)):
        order = Order.objects.create(**order_data, reseller=reseller)
        order.full_clean()
