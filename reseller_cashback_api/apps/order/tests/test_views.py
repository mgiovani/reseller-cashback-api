import json

import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from apps.order.models import OrderStatus

pytestmark = pytest.mark.django_db


def test_order_endpoint_list_orders(api_client, order):
    reversed_url = reverse('order')
    response = api_client.get(path=reversed_url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == 1
    assert response_data[0]['code'] == order.code
    assert response_data[0]['price'] == str(order.price)
    assert response_data[0]['date'] == order.date.isoformat()
    assert response_data[0]['status'] == order.status
    assert 'reseller' in response_data[0]


@pytest.mark.parametrize(
    "required_field", ['code', 'price', 'date', 'cpf'])
def test_order_endpoint_cannot_create_order_without_required_fields(
        api_client, order_data, required_field, reseller_data):

    order_data = order_data | {'cpf': reseller_data['cpf']}
    del order_data[required_field]
    reversed_url = reverse('order')
    response = api_client.post(path=reversed_url, data=order_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert required_field in response_data
    assert len(response_data[required_field]) == 1
    assert 'is required' in response_data[required_field][0]


def test_order_endpoint_can_create_order_with_valid_data_approved(
        api_client, order_data, fixed_order, reseller_data):
    order_data = order_data | {'cpf': reseller_data['cpf'], 'code': 'ANOTHER'}
    reversed_url = reverse('order')
    response = api_client.post(path=reversed_url, data=order_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data['code'] == order_data['code']
    assert response_data['price'] == order_data['price']
    assert response_data['date'] == order_data['date']
    assert response_data['status'] == OrderStatus.APPROVED.name
    assert 'reseller' in response_data


def test_order_endpoint_can_create_order_with_valid_data_validation(
        api_client, order_data, reseller, fixed_order):
    order_data = order_data | {'cpf': reseller.cpf, 'code': 'ANOTHER'}
    reversed_url = reverse('order')
    response = api_client.post(path=reversed_url, data=order_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data['code'] == order_data['code']
    assert response_data['price'] == order_data['price']
    assert response_data['date'] == order_data['date']
    assert response_data['status'] == OrderStatus.VALIDATION.name
    assert 'reseller' in response_data


@pytest.mark.parametrize('method', ['put', 'patch', 'delete'])
def test_order_endpoint_cannot_update_order_with_approved_status(
        api_client, fixed_order, method, order_data, reseller):
    reversed_url = reverse('order')
    response = api_client.get(path=reversed_url)
    response_data = response.json()
    order_id = response_data[0]['id']

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == 1
    assert response_data[0]['status'] == OrderStatus.APPROVED.name

    order_data = order_data | {'cpf': reseller.cpf, 'code': 'CHANGED'}
    response = api_client.generic(
        method=method,
        path=f'{reversed_url}{order_id}/',
        data=json.dumps(order_data),
        content_type='application/json')
    response_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'order' in response_data
    assert 'Cannot change completed orders' in response_data['order']
