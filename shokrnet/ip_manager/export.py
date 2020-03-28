from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .resources import *


@login_required
def exportLocationCSV(request):
    person_resource = LocationResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="network_locations.csv"'
    return response


@login_required
def exportLocationJSON(request):
    person_resource = LocationResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="network_locations.json"'
    return response


@login_required
def exportLocationXLS(request):
    person_resource = LocationResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="network_locations.xls"'
    return response
