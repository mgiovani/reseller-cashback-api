from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, UserManager, PermissionsMixin
)


class ResellerManager(UserManager):

    def create_superuser(self, email, password, **kwargs):
        user = Reseller.objects.create(
            email=email, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class Reseller(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=120, blank=False, null=False)
    cpf = models.CharField(
        max_length=14, unique=True, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = ResellerManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ('email, password', 'name', 'cpf')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
