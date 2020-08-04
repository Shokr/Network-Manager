from django.urls import path

from .views import *

app_name = "ip_manager"

urlpatterns = [
    path("", home, name="home"),
    path("ip/", IPListView.as_view(), name="list_ip"),
    path("ip/add/", IPCreate.as_view(), name="add_ip"),
    path("ip/update/<int:pk>/", IPUpdate.as_view(), name="update_ip"),
    path("ip/<int:pk>/", IPDetailView.as_view(), name="detail_ip"),
    path("ip/delete/<int:pk>/", delete_ip, name="delete_ip"),
    path("subnet/", SubnetListView.as_view(), name="list_subnet"),
    path("subnet/add/", SubnetCreate.as_view(), name="add_subnet"),
    path("subnet/update/<int:pk>/", SubnetUpdate.as_view(), name="update_subnet"),
    path("subnet/<int:pk>/", SubnetDetailView.as_view(), name="detail_subnet"),
    path("subnet/delete/<int:pk>/", delete_subnet, name="delete_subnet"),
    path("subnet/ip_list/<int:pk>/", subnet_ips, name="subnet_ips"),
    path("vlan/", VLANListView.as_view(), name="list_vlan"),
    path("vlan/add/", VLANCreate.as_view(), name="add_vlan"),
    path("vlan/update/<int:pk>/", VLANUpdate.as_view(), name="update_vlan"),
    path("vlan/<int:pk>/", VLANDetailView.as_view(), name="detail_vlan"),
    path("vlan/delete/<int:pk>/", delete_VLAN, name="delete_vlan"),
    #
    path("service/", ServiceListView.as_view(), name="list_service"),
    path("service/add/", ServiceCreate.as_view(), name="add_service"),
    path("service/update/<int:pk>/", ServiceUpdate.as_view(), name="update_service"),
    path("service/<int:pk>/", ServiceDetailView.as_view(), name="detail_service"),
    path("service/delete/<int:pk>/", delete_Service, name="delete_service"),
    path("device/", DeviceListView.as_view(), name="list_device"),
    path("device/add/", DeviceCreate.as_view(), name="add_device"),
    path("device/update/<int:pk>/", DeviceUpdate.as_view(), name="update_device"),
    path("device/<int:pk>/", DeviceDetailView.as_view(), name="detail_device"),
    path("device/delete/<int:pk>/", delete_Device, name="delete_device"),
    path("deviceType/", DeviceTypeListView.as_view(), name="list_device_type"),
    path("deviceType/add/", DeviceTypeCreate.as_view(), name="add_device_type"),
    path(
        "deviceType/update/<int:pk>/",
        DeviceTypeUpdate.as_view(),
        name="update_device_type",
    ),
    path(
        "deviceType/<int:pk>/",
        DeviceTypeDetailView.as_view(),
        name="detail_device_type",
    ),
    path("deviceType/delete/<int:pk>/", delete_DeviceType, name="delete_device_type"),
    path("location/", LocationListView.as_view(), name="list_location"),
    path("location/add/", LocationCreate.as_view(), name="add_location"),
    path("location/update/<int:pk>/", LocationUpdate.as_view(), name="update_location"),
    path("location/<int:pk>/", LocationDetailView.as_view(), name="detail_location"),
    path("location/delete/<int:pk>/", delete_Location, name="delete_location"),
    # # # EXPORTING
    # path('ip/csv', exportIPCSV, name='IPCSV'),
    # path('ip/json', exportIPJSON, name='IPJSON'),
    # path('ip/xls', exportIPXLS, name='IPXLS'),
]

# path('delete/<int:pk>/', IPDelete.as_view(), name='delete_ip'),
