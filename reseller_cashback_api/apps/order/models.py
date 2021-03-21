from decimal import Decimal, getcontext
from enum import Enum

from django.db import models

from apps.reseller.models import Reseller


class OrderStatus(str, Enum):
    APPROVED = "Approved"
    VALIDATION = "Validation"


class Order(models.Model):

    code = models.CharField(
        max_length=20, unique=True, blank=False, null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()
    status = models.CharField(
        max_length=30,
        choices=[(order.name, order.value) for order in OrderStatus],
        default=OrderStatus.VALIDATION.name)
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.reseller.cpf == '153.509.460-56':
            self.status = OrderStatus.APPROVED.name
        return super().save(*args, **kwargs)

    @property
    def cashback_percent(self):
        if self.price <= Decimal('1000'):
            return '0.10'
        if self.price <= Decimal('1500'):
            return '0.15'
        if self.price > Decimal('1500'):
            return '0.20'

    @property
    def cashback_total(self):
        cashback_total = round(self.price * Decimal(self.cashback_percent), 2)
        return str(cashback_total)
