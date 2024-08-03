from django.db import models

from user.models import Employee


# Create your models here.
class Transaction(models.Model):
    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "transaction_id",
                ]
            ),
        ]
        ordering = ("-transaction_date",)

    transaction_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    amount = models.FloatField()
    transaction_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions"
    )

    def save(self, *args, **kwargs):
        if self._state.adding:
            transaction_prefix = "TXNID"
            self.transaction_id = transaction_prefix + self.id

        super().save(*args, **kwargs)
