from rest_framework.serializers import ModelSerializer

from shokrnet.ip_manager.models import *


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class DeviceTypeSerializer(ModelSerializer):
    class Meta:
        model = DeviceType
        fields = '__all__'


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class SubnetSerializer(ModelSerializer):
    class Meta:
        model = Subnet
        fields = '__all__'


class IPSerializer(ModelSerializer):
    class Meta:
        model = IPAddress
        fields = '__all__'


class VLANSerializer(ModelSerializer):
    class Meta:
        model = VLAN
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
