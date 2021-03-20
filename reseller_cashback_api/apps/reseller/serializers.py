from rest_framework import serializers

from apps.reseller.models import Reseller


class ResellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reseller
        fields = ('name', 'cpf', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        reseller = Reseller(**validated_data)
        reseller.set_password(validated_data['password'])
        reseller.save()
        return reseller
