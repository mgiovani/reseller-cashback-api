import pytest

from apps.reseller.serializers import ResellerSerializer

pytestmark = pytest.mark.django_db


@pytest.fixture
def reseller_valid_data(reseller_data, user_data):
    return reseller_data | {'user': user_data}


def test_reseller_serializer_is_valid_with_all_fields(reseller_valid_data):
    serializer = ResellerSerializer(data=reseller_valid_data)
    assert serializer.is_valid() is True


@pytest.mark.parametrize("required_field", ['name', 'cpf', 'user'])
def test_reseller_serializer_is_not_valid_without_required_fields(
        reseller_valid_data, required_field):
    del reseller_valid_data[required_field]

    serializer = ResellerSerializer(data=reseller_valid_data)
    assert serializer.is_valid() is False
