from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from shokrnet.ip_manager.models import Site, Device, DeviceType, Subnet, IPAddress, VLAN, Service
from shokrnet.ip_manager.serializers import SiteSerializer, DeviceSerializer, DeviceTypeSerializer, SubnetSerializer, \
    IPSerializer, VLANSerializer, ServiceSerializer


class SiteViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Site.objects.all()
    serializer_class = SiteSerializer


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
