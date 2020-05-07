from rest_framework import serializers
from .models import GoldRates, GoldMaster


class GoldRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GoldRates
        # fields = '__all__'
        fields = "__all__"


class GoldMasterSerializer(serializers.ModelSerializer):
    golddetails = GoldRateSerializer(many=True, read_only=True)
    class Meta:
        model = GoldMaster
        fields = ('id','Particulars','Units','golddetails')