from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from shokrnet.ip_manager.models import (
    VLAN,
    Device,
    DeviceType,
    IPAddress,
    Location,
    Service,
    Subnet,
)
from shokrnet.ip_manager.serializers import (
    DeviceSerializer,
    DeviceTypeSerializer,
    IPSerializer,
    LocationSerializer,
    ServiceSerializer,
    SubnetSerializer,
    VLANSerializer,
)


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
