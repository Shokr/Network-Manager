from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from shokrnet.ip_manager.forms import *


# IP


class IPCreate(CreateView):
    model = IPAddress
    fields = ['subnet', 'address', 'status', 'role', 'device', 'nat_inside', 'dns_name', 'description']


class IPUpdate(UpdateView):
    model = IPAddress
    fields = ['subnet', 'address', 'status', 'role', 'device', 'nat_inside', 'dns_name', 'description']


# class IPDelete(DeleteView):
#     model = IPAddress
#     success_url = reverse_lazy('ip_manager:home')


class IPDetailView(DetailView):
    model = IPAddress


class IPListView(ListView):
    model = IPAddress
    # paginate_by = 50


@login_required
def delete_ip(request, pk):
    ip = get_object_or_404(IPAddress, pk=pk)
    ip.delete()
    return redirect('ip_manager:ip_list')


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

#######################################################################################################################
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
