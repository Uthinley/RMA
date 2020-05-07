from django.shortcuts import render 
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import GoldRateSerializer, GoldMasterSerializer
from .models import GoldRates, GoldMaster

# Create your views here.
@api_view(['GET'])
def apiover(request):
    api_urls = {
        'List': '/goldrates/',
        'detail': '/goldsilverdetail/<str:pk>/',
    }
    return Response(api_urls)

# for whole fileds and data
@api_view(['GET'])
def Goldlist(request):
    # gold = GoldRates.objects.all()
    gold = GoldMaster.objects.filter().select_related()
    serializer = GoldMasterSerializer(gold, many=True)
  
    return Response(serializer.data)

# for speicific data
@api_view(['GET'])
def GoldlistDetail(request,id):
    # gold = GoldRates.objects.get(id=id)
    gold = GoldMaster.objects.filter(id=id).select_related()
    # serializer = GoldRateSerializer(gold, many=False)
    serializer = GoldMasterSerializer(gold, many=True)
    return Response(serializer.data)