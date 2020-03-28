from import_export.resources import ModelResource

from .models import *


class LocationResource(ModelResource):
    class Meta:
        model = Location
        fields = '__all__'


class DeviceTypeResource(ModelResource):
    class Meta:
        model = DeviceType
        fields = '__all__'


class DeviceResource(ModelResource):
    class Meta:
        model = Device
        fields = '__all__'


class SubnetResource(ModelResource):
    class Meta:
        model = Subnet
        fields = '__all__'


class IPResource(ModelResource):
    class Meta:
        model = IPAddress
        fields = '__all__'


class VLANResource(ModelResource):
    class Meta:
        model = VLAN
        fields = '__all__'


class ServiceResource(ModelResource):
    class Meta:
        model = Service
        fields = '__all__'
