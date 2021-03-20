from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView)
from rest_framework.serializers import ValidationError

from .models import Order, OrderStatus
from .serializers import OrderSerializer


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != OrderStatus.VALIDATION.name:
            raise ValidationError(
                {'order': 'cannot change completed orders'})
        return super().destroy(self, request, *args, **kwargs)
