from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    amount = models.FloatField()
    transaction_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_id


@receiver(post_save, sender=Transaction)
def save_transaction_id(sender, instance, **kwargs):
    if kwargs.get("created"):
        transaction_prefix = "TXNID"
        instance.transaction_id = transaction_prefix + str(instance.pk)
        instance.save()
