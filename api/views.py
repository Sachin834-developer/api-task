from django.shortcuts import render
from .models import Commodity
from .serializers import CommoditySerialzer

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def commodity_list(request):
    if request.method == 'GET':
        commodities=Commodity.objects.all()
        serializer=CommoditySerialzer(commodities,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=CommoditySerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT','GET','DELETE'])
def commodity_detail(request,pk):
    try:
        commodity=Commodity.objects.get(pk=pk)
    except Commodity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=CommoditySerialzer(commodity)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer =CommoditySerialzer(commodity,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        commodity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)