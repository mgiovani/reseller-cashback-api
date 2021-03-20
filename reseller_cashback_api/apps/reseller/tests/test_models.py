import pytest
from django.db.utils import IntegrityError

from ..models import Reseller

pytestmark = pytest.mark.django_db


def test_reseller_model_can_be_created(user, reseller_data):
    reseller = Reseller.objects.create(user=user, **reseller_data)
    assert isinstance(reseller, Reseller)
    assert reseller.name == reseller_data['name']
    assert reseller.cpf == reseller_data['cpf']


@pytest.mark.parametrize("required_field", ['name', 'cpf'])
def test_reseller_model_cannot_be_created_without_name(
        reseller_data, required_field):
    del reseller_data[required_field]

    with pytest.raises(IntegrityError):
        Reseller.objects.create(**reseller_data)
