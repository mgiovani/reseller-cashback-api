from django.db import models
from django.contrib.auth.models import User


class Reseller(models.Model):
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
