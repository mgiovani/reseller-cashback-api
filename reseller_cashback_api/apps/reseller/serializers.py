from rest_framework import serializers
from django.contrib.auth.models import User

from apps.reseller.models import Reseller


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'date_joined')


class ResellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        reseller = Reseller.objects.create(user=user, **validated_data)
        return reseller

    class Meta:
        model = Reseller
        fields = ('name', 'cpf', 'user')
