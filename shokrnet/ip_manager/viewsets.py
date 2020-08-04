from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from shokrnet.ip_manager.models import Device
from shokrnet.ip_manager.models import DeviceType
from shokrnet.ip_manager.models import IPAddress
from shokrnet.ip_manager.models import Location
from shokrnet.ip_manager.models import Service
from shokrnet.ip_manager.models import Subnet
from shokrnet.ip_manager.models import VLAN
from shokrnet.ip_manager.serializers import DeviceSerializer
from shokrnet.ip_manager.serializers import DeviceTypeSerializer
from shokrnet.ip_manager.serializers import IPSerializer
from shokrnet.ip_manager.serializers import LocationSerializer
from shokrnet.ip_manager.serializers import ServiceSerializer
from shokrnet.ip_manager.serializers import SubnetSerializer
from shokrnet.ip_manager.serializers import VLANSerializer


class LocationViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DeviceTypeViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer


class DeviceViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SubnetViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer


class IPViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = IPAddress.objects.all()
    serializer_class = IPSerializer


class VLANViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer


class ServiceViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
