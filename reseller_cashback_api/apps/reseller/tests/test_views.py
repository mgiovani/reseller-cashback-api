import pytest
from rest_framework import status
from rest_framework.reverse import reverse


pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('method', ['put', 'patch', 'delete'])
def test_reseller_endpoint_methods_not_allowed(method, api_client):
    reversed_url = reverse('reseller')
    response = api_client.generic(method=method, path=reversed_url, data={})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_reseller_endpoint_list_resellers(api_client, reseller):
    reversed_url = reverse('reseller')
    response = api_client.get(path=reversed_url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == 1
    assert response_data[0]['name'] == reseller.name
    assert response_data[0]['cpf'] == reseller.cpf
    assert response_data[0]['email'] == reseller.email


@pytest.mark.parametrize(
    "required_field", ['name', 'cpf', 'email', 'password'])
def test_reseller_endpoint_cannot_create_reseller_without_required_fields(
        api_client, reseller_data, required_field):

    del reseller_data[required_field]
    reversed_url = reverse('reseller')
    response = api_client.post(path=reversed_url, data=reseller_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert required_field in response_data
    assert len(response_data[required_field]) == 1
    assert 'is required' in response_data[required_field][0]


def test_reseller_endpoint_can_create_reseller_with_valid_data(
        api_client, reseller_data):
    reversed_url = reverse('reseller')
    response = api_client.post(path=reversed_url, data=reseller_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert reseller_data['name'] == response_data['name']
    assert reseller_data['cpf'] == response_data['cpf']
    assert reseller_data['email'] == response_data['email']


@pytest.mark.parametrize('method', ['put', 'patch', 'delete', 'get'])
def test_login_endpoint_methods_not_allowed(method, api_client):
    reversed_url = reverse('login')
    response = api_client.generic(method=method, path=reversed_url, data={})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.parametrize(
    "required_field", ['email', 'password'])
def test_login_endpoint_cannot_check_without_required_fields(
        api_client, reseller_data, required_field):

    del reseller_data[required_field]
    reversed_url = reverse('login')
    response = api_client.post(path=reversed_url, data=reseller_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert required_field in response_data
    assert len(response_data[required_field]) == 1
    assert 'is required' in response_data[required_field][0]


def test_reseller_endpoint_can_check_credentials(
        api_client, fixed_reseller, reseller_data):
    credentials = {
        'email': reseller_data['email'],
        'password': reseller_data['password']}

    reversed_url = reverse('login')
    response = api_client.post(path=reversed_url, data=credentials)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 'status' in response_data
    assert 'OK' in response_data['status']


def test_reseller_endpoint_can_check_wrong_credentials(
        api_client, reseller):
    credentials = {
        'email': reseller.email,
        'password': 'wrong_password'}

    reversed_url = reverse('login')
    response = api_client.post(path=reversed_url, data=credentials)
    response_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response_data
    assert 'Wrong credentials' in response_data['error']
