from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .forms import *


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    form = LocationForm

    search_fields = ('name', 'address')

    list_display = (
        'name',
        'address',
        'geolocation',
    )

    readonly_fields = (
        'time_created',
    )


@admin.register(DeviceType)
class DeviceTypeAdmin(ImportExportModelAdmin):
    form = DeviceTypeForm

    search_fields = ('name', 'model_number')

    list_display = (
        'name',
        'model_number',
        'manufacturer',
    )

    readonly_fields = (
        'time_created',
    )


@admin.register(Device)
class DeviceAdmin(ImportExportModelAdmin):
    form = DeviceForm

    search_fields = ('name', 'serial_number')

    list_display = (
        'name',
        'serial_number',
        'device_type',
    )

    readonly_fields = (
        'time_created',
    )


@admin.register(Subnet)
class SubnetAdmin(ImportExportModelAdmin):
    form = SubnetForm

    search_fields = ('name', 'subnet')

    list_display = (
        'name',
        'subnet',
        'family',
        'broadcast_address',
        'utilization_percentage',
        'master_subnet',
        'vlan',
    )

    readonly_fields = (
        'family',
        'broadcast_address',
        'utilization_percentage',
        'hostmask',
        'netmask',
        'total_hosts',
        'reserved_hosts',
        'time_created',
    )


@admin.register(IPAddress)
class IPAddressAdmin(ImportExportModelAdmin):
    form = IPForm

    search_fields = ('address', 'subnet')

    list_display = (
        'address',
        'subnet',
        'status',
        'role',
        'nat_inside',
        'device',
        'dns_name',
    )

    readonly_fields = (
        'time_created',
    )


@admin.register(VLAN)
class VLANAdmin(ImportExportModelAdmin):
    form = VLANForm

    search_fields = ('name', 'vid')

    list_display = (
        'vid',
        'name',
        'status',
    )

    readonly_fields = (
        'time_created',
    )


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    form = ServiceForm

    search_fields = ('name',)

    readonly_fields = (
        'time_created',
    )

# admin.site.register(Service)
