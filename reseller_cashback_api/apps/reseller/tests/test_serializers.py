import pytest

from apps.reseller.serializers import (
    ResellerSerializer, ResellerLoginSerializer)

pytestmark = pytest.mark.django_db


def test_reseller_serializer_is_valid_with_all_fields(reseller_data):
    serializer = ResellerSerializer(data=reseller_data)
    assert serializer.is_valid() is True


@pytest.mark.parametrize(
    "required_field", ['name', 'cpf', 'email', 'password'])
def test_reseller_serializer_is_not_valid_without_required_fields(
        reseller_data, required_field):
    del reseller_data[required_field]

    serializer = ResellerSerializer(data=reseller_data)
    assert serializer.is_valid() is False


def test_reseller_login_serializer_is_valid_with_all_fields(
        reseller_data, fixed_reseller):
    serializer = ResellerLoginSerializer(data=reseller_data)
    assert serializer.is_valid() is True


@pytest.mark.parametrize(
    "required_field", ['email', 'password'])
def test_reseller_login_serializer_is_not_valid_without_required_fields(
        reseller_data, required_field, fixed_reseller):
    del reseller_data[required_field]

    serializer = ResellerLoginSerializer(data=reseller_data)
    assert serializer.is_valid() is False
