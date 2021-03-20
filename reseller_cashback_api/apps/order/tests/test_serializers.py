import pytest

from apps.order.serializers import OrderSerializer

pytestmark = pytest.mark.django_db


def test_order_serializer_is_valid_with_all_fields(order_data, reseller_data):
    order_data = order_data | {'cpf': reseller_data['cpf']}
    serializer = OrderSerializer(data=order_data)
    assert serializer.is_valid() is True


@pytest.mark.parametrize(
    "required_field", ['code', 'price', 'date', 'cpf'])
def test_order_serializer_is_not_valid_without_required_fields(
        order_data, required_field, reseller_data):
    order_data = order_data | {'cpf': reseller_data['cpf']}
    del order_data[required_field]

    serializer = OrderSerializer(data=order_data)
    assert serializer.is_valid() is False
