from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from shokrnet.ip_manager.viewsets import (
    DeviceTypeViewSet,
    DeviceViewSet,
    IPViewSet,
    LocationViewSet,
    ServiceViewSet,
    SubnetViewSet,
    VLANViewSet,
)
from shokrnet.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register("locations", LocationViewSet)
router.register("device_types", DeviceTypeViewSet)
router.register("devices", DeviceViewSet)
router.register("subnets", SubnetViewSet)
router.register("ips", IPViewSet)
router.register("vlans", VLANViewSet)
router.register("services", ServiceViewSet)

app_name = "api"
urlpatterns = router.urls
