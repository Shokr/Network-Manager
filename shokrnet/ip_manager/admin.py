from django.contrib import admin

from .models import *

admin.site.register(Location)
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(Subnet)
admin.site.register(IPAddress)
admin.site.register(VLAN)
admin.site.register(Service)
