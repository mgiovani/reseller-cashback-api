import pytest

from apps.reseller.serializers import ResellerSerializer

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
