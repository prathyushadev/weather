from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from wapi.models import Weather
from wapi.serializer import WeatherSerializer

# Create your views here.


class WeatherViewSet(ViewSet):
    def list(self, request):
        queryset = Weather.objects.all()
        serializer = WeatherSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Weather.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = WeatherSerializer(user)
        return Response(serializer.data)


class WeatherStatsViewset(ViewSet):
    def list(self, request):
        queryset = Weather.objects.all()
        serializer = WeatherSerializer(queryset, many=True)
        return Response(serializer.data)
