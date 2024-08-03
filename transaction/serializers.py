from rest_framework import serializers
from .models import Transaction

class TransactionReadSerializer(serializers.Serializer):
    transaction_id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    transaction_date = serializers.DateField(read_only=True)
    amount = serializers.FloatField(read_only=True)


class TransactionWriteSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    transaction_date = serializers.DateField()
    amount = serializers.FloatField()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)
    