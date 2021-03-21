from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView)
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from .api import ExternalAPI
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
                {'order': 'Cannot change completed orders'})
        return super().destroy(self, request, *args, **kwargs)


class AccumulatedCashbackView(APIView):

    def get(self, request):
        external_api = ExternalAPI()
        response, status_code = external_api.get_accumulated_cashback(
            self.request.query_params)
        return Response(response, status=status_code)
