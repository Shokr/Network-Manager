from django.urls import path

from .views import *

app_name = 'ip_manager'

urlpatterns = [
    path('', home, name='home'),

    path('ip/', IPListView.as_view(), name='list_ip'),
    path('ip/add/', IPCreate.as_view(), name='add_ip'),
    path('ip/update/<int:pk>/', IPUpdate.as_view(), name='update_ip'),
    path('ip/<int:pk>/', IPDetailView.as_view(), name='detail_ip'),
    path('ip/delete/<int:pk>/', delete_ip, name='delete_ip'),

    path('subnet/', SubnetListView.as_view(), name='list_subnet'),
    path('subnet/add/', SubnetCreate.as_view(), name='add_subnet'),
    path('subnet/update/<int:pk>/', SubnetUpdate.as_view(), name='update_subnet'),
    path('subnet/<int:pk>/', SubnetDetailView.as_view(), name='detail_subnet'),
    path('subnet/delete/<int:pk>/', delete_subnet, name='delete_subnet'),

    path('vlan/', VLANListView.as_view(), name='list_vlan'),
    path('vlan/add/', VLANCreate.as_view(), name='add_vlan'),
    path('vlan/update/<int:pk>/', VLANUpdate.as_view(), name='update_vlan'),
    path('vlan/<int:pk>/', VLANDetailView.as_view(), name='detail_vlan'),
    path('vlan/delete/<int:pk>/', delete_VLAN, name='delete_vlan'),
    #
    # path('service/', SubnetListView.as_view(), name='list_subnet'),
    # path('service/add/', SubnetCreate.as_view(), name='add_subnet'),
    # path('service/update/<int:pk>/', SubnetUpdate.as_view(), name='update_subnet'),
    # path('service/<int:pk>/', SubnetDetailView.as_view(), name='detail_subnet'),
    # path('service/delete/<int:pk>/', delete_subnet, name='delete_subnet'),
    #
    # path('device/', SubnetListView.as_view(), name='list_subnet'),
    # path('device/add/', SubnetCreate.as_view(), name='add_subnet'),
    # path('device/update/<int:pk>/', SubnetUpdate.as_view(), name='update_subnet'),
    # path('device/<int:pk>/', SubnetDetailView.as_view(), name='detail_subnet'),
    # path('device/delete/<int:pk>/', delete_subnet, name='delete_subnet'),
    #
    # path('deviceType/', SubnetListView.as_view(), name='list_subnet'),
    # path('deviceType/add/', SubnetCreate.as_view(), name='add_subnet'),
    # path('deviceType/update/<int:pk>/', SubnetUpdate.as_view(), name='update_subnet'),
    # path('deviceType/<int:pk>/', SubnetDetailView.as_view(), name='detail_subnet'),
    # path('deviceType/delete/<int:pk>/', delete_subnet, name='delete_subnet'),

    # # EXPORTING
    # path('ip/csv', exportIPCSV, name='IPCSV'),
    # path('ip/json', exportIPJSON, name='IPJSON'),
    # path('ip/xls', exportIPXLS, name='IPXLS'),
]

# path('delete/<int:pk>/', IPDelete.as_view(), name='delete_ip'),
