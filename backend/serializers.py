from .models import Restaurant
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'url']