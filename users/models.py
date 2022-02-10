from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class KefirUser(AbstractUser):
    other_name = models.CharField(max_length=150, blank=True)
    phone = PhoneNumberField(unique=True, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.ManyToManyField(City, related_name="kefir_users")
    additional_info = models.TextField(null=True)
    is_admin = None

    def __init__(self, *args, **kwargs):
        super(KefirUser, self).__init__(*args, **kwargs)
        self.is_admin = self.is_staff

    def __str__(self):
        return f"username: {self.username}, id: {self.pk}"
