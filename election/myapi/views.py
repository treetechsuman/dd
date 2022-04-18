from django.shortcuts import render
from rest_framework import viewsets

from myapi.serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer
from address.models import District, Province,Municipality

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all().order_by('name')
    serializer_class = ProvinceSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by('name')
    serializer_class = DistrictSerializer

class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all().order_by('name')
    serializer_class = MunicipalitySerializer

