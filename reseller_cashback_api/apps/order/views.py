from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView)

from .models import Order
from .serializers import OrderSerializer


class OrderView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
