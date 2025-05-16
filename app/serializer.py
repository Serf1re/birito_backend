from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'orders']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['title', 'description', 'complete', 'status', 'created']
