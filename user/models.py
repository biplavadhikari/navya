from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoices(models.TextChoices):
    STAFF = "Staff"
    MANAGER = "Manager"


# Create your models here.
class Employee(AbstractUser):
    employee_title = models.CharField(max_length=100, choices=RoleChoices, default=RoleChoices.STAFF)
