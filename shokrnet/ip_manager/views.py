from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from shokrnet.ip_manager.forms import *


class IPCreate(CreateView):
    model = IPAddress
    fields = ['address', 'subnet', 'status', 'role', 'device', 'nat_inside', 'dns_name', 'description']


class IPUpdate(UpdateView):
    model = IPAddress
    fields = ['address', 'subnet', 'status', 'role', 'device', 'nat_inside', 'dns_name', 'description']


class IPDelete(DeleteView):
    model = IPAddress
    success_url = reverse_lazy('ip_manager:home')


class IPDetailView(DetailView):
    model = IPAddress


class IPListView(ListView):
    model = IPAddress
    paginate_by = 50


class IPSearchResultsView(ListView):
    model = IPAddress
    template_name = 'ip_manager/ip_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = IPAddress.objects.filter(Q(address__icontains=query))
        return object_list
