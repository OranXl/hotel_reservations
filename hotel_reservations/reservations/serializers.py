from django.db import models
from rest_framework import serializers
from .models import Hotel, Reservations


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields =  '__all__'
        read_only_fields = ['id', 'create_at']


class ReservationsSerializer(serializers.ModelSerializer):
        model = Reservations
        fields = '__all__'
        read_only_fields = ['id']