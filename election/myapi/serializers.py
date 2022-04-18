from rest_framework import serializers
from address.models import District, Province,Municipality

class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    districts = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='district-detail')
    class Meta:
        model = Province
        fields = ('url','name', 'coordinate','districts')

class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    municipalities = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='municipality-detail')
    class Meta:
        model = District
        fields = ('url','province','name', 'coordinate','municipalities')

class MunicipalitySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Municipality
        fields = ('url','district','name', 'coordinate')