import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from management.models import Address


class Account(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4)
    is_admin = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=12, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
