from rest_framework import serializers
from .models import Customer, FavoriteList


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = [
            'id',
            'customer_id',
            'product_id'
        ]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'email'
        ]
