from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

from .models import Combo
from .serializers import *

# Create your views here.
class ComboView(viewsets.ModelViewSet):
    serializer_class = ComboSerializer
    queryset = Combo.objects.all()

@api_view(['GET', 'POST'])
def combos_list(request):
    if request.method == 'GET':
        data = Combo.objects.all()

        serializer = ComboSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ComboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def combos_detail(request, pk):
    try:
        combo = ComboSerializer.objects.get(pk=pk)
    except Combo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ComboSerializer(combo, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        combo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)