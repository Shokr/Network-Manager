from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from shokrnet.ip_manager.forms import *


@login_required
def home(request):
    location = Location.objects.get_queryset().count()
    subnet = Subnet.objects.get_queryset().count()
    ip = IPAddress.objects.get_queryset().count()
    service = Service.objects.get_queryset().count()
    device = Device.objects.get_queryset().count()
    deviceType = DeviceType.objects.get_queryset().count()
    vlan = VLAN.objects.get_queryset().count()

    user = request.user

    return render(request, 'ip_manager/home',
                  {'user': user, 'location': location, 'subnet': subnet, 'ip': ip,
                   'service': service, 'device': device,
                   'device_type': deviceType, 'vlan': vlan})


# IP


class IPCreate(CreateView):
    model = IPAddress
    fields = ['subnet', 'address', 'status', 'role', 'device', 'nat_inside', 'dns_name', 'description']

    def get_success_url(self):
        return reverse('ip_manager:list_ip')


class IPUpdate(UpdateView):
    model = IPAddress
    fields = ['subnet', 'address', 'status', 'role', 'device', 'nat_inside', 'dns_name', 'description']


class IPDetailView(DetailView):
    model = IPAddress


class IPListView(ListView):
    model = IPAddress
    # paginate_by = 50


@login_required
def delete_ip(request, pk):
    ip = get_object_or_404(IPAddress, pk=pk)
    subnet = ip.subnet.pk
    reserved_hosts = Subnet.objects.get(pk=subnet).reserved_hosts
    total_hosts = Subnet.objects.get(pk=subnet).total_hosts
    Subnet.objects.filter(pk=subnet).update(reserved_hosts=reserved_hosts - 1,
                                            utilization_percentage=(reserved_hosts / total_hosts) * 100)
    ip.delete()
    return redirect('ip_manager:list_ip')


# Subnet

class SubnetCreate(CreateView):
    model = Subnet
    fields = ['name', 'subnet', 'description', 'master_subnet', 'vlan']


class SubnetUpdate(UpdateView):
    model = Subnet
    fields = ['name', 'subnet', 'description', 'master_subnet', 'vlan']


class SubnetDetailView(DetailView):
    model = Subnet


class SubnetListView(ListView):
    model = Subnet


@login_required
def delete_subnet(request, pk):
    subnet = get_object_or_404(Subnet, pk=pk)
    subnet.delete()
    return redirect('ip_manager:list_subnet')


# VLAN

class VLANCreate(CreateView):
    model = VLAN
    fields = ['name', 'location', 'vid', 'status', 'description']


class VLANUpdate(UpdateView):
    model = VLAN
    fields = ['name', 'location', 'vid', 'status', 'description']


class VLANDetailView(DetailView):
    model = VLAN


class VLANListView(ListView):
    model = VLAN


@login_required
def delete_VLAN(request, pk):
    vlan = get_object_or_404(VLAN, pk=pk)
    vlan.delete()
    return redirect('ip_manager:list_vlan')


# Service

class ServiceCreate(CreateView):
    model = Service
    fields = ['name', 'protocol', 'ip_addresses', 'port', 'description']


class ServiceUpdate(UpdateView):
    model = Service
    fields = ['name', 'protocol', 'ip_addresses', 'port', 'description']


class ServiceDetailView(DetailView):
    model = Service


class ServiceListView(ListView):
    model = Service


@login_required
def delete_Service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('ip_manager:list_service')


# Device

class DeviceCreate(CreateView):
    model = Device
    fields = ['name', 'serial_number', 'mac', 'device_type']


class DeviceUpdate(UpdateView):
    model = Device
    fields = ['name', 'serial_number', 'mac', 'device_type']


class DeviceDetailView(DetailView):
    model = Device


class DeviceListView(ListView):
    model = Device


@login_required
def delete_Device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    return redirect('ip_manager:list_device')


# Device Type

class DeviceTypeCreate(CreateView):
    model = DeviceType
    fields = ['manufacturer', 'model_number', 'name']


class DeviceTypeUpdate(UpdateView):
    model = DeviceType
    fields = ['manufacturer', 'model_number', 'name']


class DeviceTypeDetailView(DetailView):
    model = DeviceType


class DeviceTypeListView(ListView):
    model = DeviceType


@login_required
def delete_DeviceType(request, pk):
    device_type = get_object_or_404(DeviceType, pk=pk)
    device_type.delete()
    return redirect('ip_manager:list_device_type')


# Location

class LocationCreate(CreateView):
    model = Location
    fields = ['name', 'geolocation', 'address']


class LocationUpdate(UpdateView):
    model = Location
    fields = ['name', 'geolocation', 'address']


class LocationDetailView(DetailView):
    model = Location


class LocationListView(ListView):
    model = Location


@login_required
def delete_Location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    location.delete()
    return redirect('ip_manager:list_location')


@login_required
def subnet_ips(request, pk):
    subnet = get_object_or_404(Subnet, pk=pk)
    used_ips = IPAddress.objects.filter(subnet=subnet).values_list('address', flat=True)
    ip_list = list(ipaddress.ip_network(subnet.subnet).hosts())
    free_ips = list(set(ip_list) - set(used_ips))

    return render(request, 'ip_manager/subnet_ip_list.html', {'subnet': subnet, 'usedIPS': used_ips,
                                                              'freeIPS': free_ips})
#######################################################################################################################
#

# class IPDelete(DeleteView):
#     model = IPAddress
#     success_url = reverse_lazy('ip_manager:home')
#
#
# @login_required
# def exportIPCSV(request):
#     resource = IPResource()
#     dataset = resource.export()
#     response = HttpResponse(dataset.csv, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="network_IPs.csv"'
#     return response
#
#
# @login_required
# def exportIPJSON(request):
#     resource = IPResource()
#     dataset = resource.export()
#     response = HttpResponse(dataset.json, content_type='application/json')
#     response['Content-Disposition'] = 'attachment; filename="network_IPs.json"'
#     return response
#
#
# @login_required
# def exportIPXLS(request):
#     resource = IPResource()
#     dataset = resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="network_IPs.xls"'
#     return response
