from unittest import mock

import pytest

from apps.order.api import ExternalAPI


@pytest.fixture
def error_response_api():
    return {
        'statusCode': 400,
        'body': {
            'message': 'CPF do revendedor(a) está incorreto, '
            'utilize apenas números!'
        }
    }


@pytest.fixture
def ok_response_api():
    return {
        'statusCode': 200,
        'body': {
            'credit': 3029,
        }
    }


@pytest.fixture
def client_api():
    client_api = ExternalAPI()
    client_api.EXTERNAL_API_BASE_URL = 'base_url/'
    client_api.EXTERNAL_API_TOKEN = 'token'
    client_api.AUTHORIZATION = {'token': 'token'}
    return client_api


def test_external_api_get_full_path(client_api):
    full_url = client_api._get_full_path('test/?id=1')
    assert full_url == 'base_url/test/?id=1'


def test_external_api_get_formatted_response(client_api, ok_response_api):
    mock_response = mock.Mock()
    mock_response.json.return_value = ok_response_api
    formatted_response = client_api._get_formatted_response(mock_response)
    expected_response = {'credit': 3029}
    assert formatted_response == expected_response


def test_external_api_get_status_code(client_api, ok_response_api):
    mock_response = mock.Mock()
    mock_response.json.return_value = ok_response_api
    status_code = client_api._get_status_code(mock_response)
    assert status_code == 200


def test_external_api_get_formatted_response_error(
        client_api, error_response_api):
    mock_response = mock.Mock()
    mock_response.json.return_value = error_response_api
    formatted_response = client_api._get_formatted_response(mock_response)
    assert 'message' in formatted_response
    assert 'CPF' in formatted_response['message']


def test_external_api_get_status_code_response_error(
        client_api, error_response_api):
    mock_response = mock.Mock()
    mock_response.json.return_value = error_response_api
    status_code = client_api._get_status_code(mock_response)
    assert status_code == 400


def test_external_api_get_method_correct_call(client_api):
    with mock.patch('apps.order.api.requests.get') as mock_get:
        client_api.get('test/?id=1')

        mock_get.assert_called_once_with(
            'base_url/test/?id=1', headers={'token': 'token'}, params={})
