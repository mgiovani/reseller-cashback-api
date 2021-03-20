from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, UserManager, PermissionsMixin
)


class Reseller(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True, primary_key=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ('email, password')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
