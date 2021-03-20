from django.contrib.auth import authenticate
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


class ResellerLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, validated_data):
        reseller = authenticate(
            email=validated_data['email'],
            password=validated_data['password'])
        if not reseller:
            raise serializers.ValidationError({'error': 'Wrong credentials'})
        return reseller
