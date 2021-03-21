from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from apps.order.models import Order, OrderStatus
from apps.reseller.models import Reseller
from apps.reseller.serializers import ResellerSerializer


class OrderSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(write_only=True)
    reseller = ResellerSerializer(required=False)

    class Meta:
        model = Order
        fields = (
            'id', 'code', 'price', 'date', 'status',
            'cpf', 'reseller', 'cashback_percent', 'cashback_total')
        read_only_fields = ('reseller', 'cashback_percent', 'cashback_total')
        extra_kwargs = {
            'price': {'required': True},
            'date': {'required': True}}

    def create(self, validated_data):
        cpf = validated_data.pop('cpf')
        try:
            reseller = Reseller.objects.get(pk=cpf)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'cpf': 'Wrong CPF'})
        order = Order.objects.create(**validated_data, reseller=reseller)
        return order

    def update(self, instance, validated_data):
        if instance.status != OrderStatus.VALIDATION.name:
            raise serializers.ValidationError(
                {'order': 'Cannot change completed orders'})
        return super().update(instance, validated_data)
