from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from json import JSONDecoder
from .models import Combo
from .serializers import *

# Create your views here.


class GameView(viewsets.ModelViewSet):
    serializer_class = gameSerializer
    queryset = Game.objects.all()

    @api_view(['GET', 'POST'])
    def game_list(request):
        if request.method == 'GET':
            data = Game.objects.all()

            serializer = gameSerializer(
                data, context={'request': request}, many=True)

            return Response(serializer.data)

        elif request.method == 'POST':
            data = request.data
            print(data)
            serializer = gameSerializer(data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT', 'DELETE'])
    def game_detail(request, pk):
        try:
            game = gameSerializer.objects.get(pk=pk)
        except Combo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = gameSerializer(
                game, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ComboView(viewsets.ModelViewSet):
    serializer_class = ComboSerializer
    queryset = Combo.objects.all()
    
    
    @api_view(['GET', 'POST'])
    def combo_list(request):
        if request.method == 'GET':
            data = Combo.objects.all()

            serializer = ComboSerializer(
                data, context={'request': request}, many=True)

            return Response(serializer.data)

        elif request.method == 'POST':
            data = request.data
            serializer = ComboSerializer(data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT', 'DELETE'])
    def combo_detail(request, pk):
        try:
            combo = ComboSerializer.objects.get(pk=pk)
        except Combo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = ComboSerializer(
                combo, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            combo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
