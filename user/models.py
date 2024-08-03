from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(AbstractUser):
    STAFF = 1
    MANAGER = 2
  
    ROLE_CHOICES = (
      (STAFF, 'Staff'),
      (MANAGER, 'Manager'),
    )
    employee_title = models.CharField(max_length=100, choices=ROLE_CHOICES, default='Staff')