from rest_framework import serializers

from apps.reseller.models import Reseller, User


class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('email', 'password', 'date_joined')
        read_only_fields = ('date_joined',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.username = validated_data['email']
        user.save()
        return user


class ResellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Reseller
        fields = ('name', 'cpf', 'user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(**user_data)
        user.set_password(user_data['password'])
        user.username = user_data['email']
        user.save()
        reseller = Reseller.objects.create(user=user, **validated_data)
        return reseller
