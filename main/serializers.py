from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ShoppingList as sl, ShoppingItem as si

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class ShoppingListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = sl
        fields = ('owner', 'list_name', 'overall_budget', 'description', 'created_on')

    def create(self, validated_data):
        # pylint: disable=no-member
        return sl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.overall_budget = validated_data['overall_budget']
        print('inst to update', instance, instance.overall_budget, validated_data)
        instance.save()
        return instance

class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = si
        fields = ('item_id', 'list_ref', 'item_name', 'description', 'category', 'price')

    def create(self, validated_data):
        # pylint: disable=no-member
        return si.objects.create(**validated_data)

        