from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from user.models import Employee


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Employee.objects.get(email=email)
            if user.check_password(password):
                return user
        except Employee.DoesNotExist:
            return None
