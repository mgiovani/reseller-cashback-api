import pytest
from django.core.exceptions import ValidationError

from ..models import Reseller

pytestmark = pytest.mark.django_db


def test_reseller_model_can_be_created(reseller_data):
    reseller = Reseller.objects.create(**reseller_data)
    assert isinstance(reseller, Reseller)
    assert reseller.name == reseller_data['name']
    assert reseller.cpf == reseller_data['cpf']
    assert reseller.email == reseller_data['email']


@pytest.mark.parametrize("required_field", ['name', 'cpf', 'email'])
def test_reseller_model_cannot_be_created_without_required_fields(
        reseller_data, required_field):

    del reseller_data[required_field]
    with pytest.raises(ValidationError):
        reseller = Reseller.objects.create(**reseller_data)
        reseller.full_clean()
