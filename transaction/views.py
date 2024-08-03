from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .permissions import IsManager
from .serializers import TransactionReadSerializer, TransactionWriteSerializer
from .utils import CustomResponse


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionReadSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "transaction_id"

    def get_queryset(self):
        return Transaction.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "partial_update", "update"]:
            return TransactionWriteSerializer
        return TransactionReadSerializer

    def get_permissions(self):
        if self.action == "destroy":
            permission_classes = [IsManager]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return CustomResponse(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return CustomResponse(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        response = self.serializer_class(instance)
        headers = self.get_success_headers(response.data)
        return CustomResponse(data=response.data, status=201, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return CustomResponse(serializer.data)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request=request, *args, **kwargs)
        return CustomResponse(status=204, message="Transaction deleted successfully")


class PDFTransactionViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Transaction.objects.all()

    def list(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass
