from django.urls import path

from .views import *

app_name = 'ip_manager'

urlpatterns = [
    path('', IPListView.as_view(), name='ip_list'),

    path('add/', IPCreate.as_view(), name='add_ip'),
    path('update/<int:pk>/', IPUpdate.as_view(), name='update_ip'),
    path('<int:pk>/', IPDetailView.as_view(), name='detail_ip'),
    path('delete/<int:pk>/', delete_ip, name='delete_ip'),

    # # EXPORTING
    # path('ip/csv', exportIPCSV, name='IPCSV'),
    # path('ip/json', exportIPJSON, name='IPJSON'),
    # path('ip/xls', exportIPXLS, name='IPXLS'),
]

# path('delete/<int:pk>/', IPDelete.as_view(), name='delete_ip'),
