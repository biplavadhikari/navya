from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"transactions", views.TransactionViewSet, basename="transactions")
router.register(r"pdf/transactions", views.PDFTransactionViewSet, basename="pdf-transactions")

urlpatterns = [
    path("", include(router.urls)),
]
