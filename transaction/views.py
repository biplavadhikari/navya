from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializers import TransactionReadSerializer, TransactionWriteSerializer
from .utils import CustomResponse
from .permissions import IsManager


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionReadSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Transaction.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["create", "partial_update", "update"]:
            return TransactionWriteSerializer
        return TransactionReadSerializer
    
    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsManager]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]
 
    def destroy(self, request, *args, **kwargs):
        super().destroy(request=request, *args, **kwargs)
        return CustomResponse(status=204)
    