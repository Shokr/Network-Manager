from django.urls import path

from . import views
from .models import *

app_name = 'ip_manager'
urlpatterns = [

    # IP addresses
    path('ip-addresses/', views.IPAddressListView.as_view(), name='ipaddress_list'),
    path('ip-addresses/add/', views.IPAddressCreateView.as_view(), name='ipaddress_add'),
    path('ip-addresses/bulk-add/', views.IPAddressBulkCreateView.as_view(), name='ipaddress_bulk_add'),
    path('ip-addresses/import/', views.IPAddressBulkImportView.as_view(), name='ipaddress_import'),
    path('ip-addresses/edit/', views.IPAddressBulkEditView.as_view(), name='ipaddress_bulk_edit'),
    path('ip-addresses/delete/', views.IPAddressBulkDeleteView.as_view(), name='ipaddress_bulk_delete'),
    path('ip-addresses/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='ipaddress_changelog',
         kwargs={'model': IPAddress}),
    path('ip-addresses/assign/', views.IPAddressAssignView.as_view(), name='ipaddress_assign'),
    path('ip-addresses/<int:pk>/', views.IPAddressView.as_view(), name='ipaddress'),
    path('ip-addresses/<int:pk>/edit/', views.IPAddressEditView.as_view(), name='ipaddress_edit'),
    path('ip-addresses/<int:pk>/delete/', views.IPAddressDeleteView.as_view(), name='ipaddress_delete'),

    # VLANs
    path('vlans/', views.VLANListView.as_view(), name='vlan_list'),
    path('vlans/add/', views.VLANCreateView.as_view(), name='vlan_add'),
    path('vlans/import/', views.VLANBulkImportView.as_view(), name='vlan_import'),
    path('vlans/edit/', views.VLANBulkEditView.as_view(), name='vlan_bulk_edit'),
    path('vlans/delete/', views.VLANBulkDeleteView.as_view(), name='vlan_bulk_delete'),
    path('vlans/<int:pk>/', views.VLANView.as_view(), name='vlan'),
    path('vlans/<int:pk>/members/', views.VLANMembersView.as_view(), name='vlan_members'),
    path('vlans/<int:pk>/edit/', views.VLANEditView.as_view(), name='vlan_edit'),
    path('vlans/<int:pk>/delete/', views.VLANDeleteView.as_view(), name='vlan_delete'),
    path('vlans/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vlan_changelog', kwargs={'model': VLAN}),

    # Services
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/import/', views.ServiceBulkImportView.as_view(), name='service_import'),
    path('services/edit/', views.ServiceBulkEditView.as_view(), name='service_bulk_edit'),
    path('services/delete/', views.ServiceBulkDeleteView.as_view(), name='service_bulk_delete'),
    path('services/<int:pk>/', views.ServiceView.as_view(), name='service'),
    path('services/<int:pk>/edit/', views.ServiceEditView.as_view(), name='service_edit'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),
    path('services/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='service_changelog',
         kwargs={'model': Service}),

]
