from enum import Enum

from django.db import models

from apps.reseller.models import Reseller


class OrderStatus(str, Enum):
    APPROVED = "Approved"
    VALIDATION = "Validation"


class Order(models.Model):

    code = models.CharField(
        max_length=20, unique=True, primary_key=True, blank=False, null=False)
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
        return super(Order, self).save(*args, **kwargs)
