from rest_framework import serializers
from .models import GoldRates


class GoldRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldRates
        fields = '__all__'