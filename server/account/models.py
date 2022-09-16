import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from management.models import Address


class Account(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4)
    phone_no = models.CharField(max_length=12, blank=True, null=True)
    birth_date = models.DateField(auto_now_add=True)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)
