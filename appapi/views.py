from django.shortcuts import render 
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import GoldRateSerializer
from .models import GoldRates

# Create your views here.
@api_view(['GET'])
def apiover(request):
    api_urls = {
        'List': '/goldrates/'
    }
    return Response(api_urls)

# for whole fileds and data
@api_view(['GET'])
def Goldlist(request):
    gold = GoldRates.objects.all()
    serializer = GoldRateSerializer(gold, many=True)
    return Response(serializer.data)

# for speicific data
@api_view(['GET'])
def GoldlistDetail(request,id):
    gold = GoldRates.objects.get(id=id)
    serializer = GoldRateSerializer(gold, many=False)
    return Response(serializer.data)