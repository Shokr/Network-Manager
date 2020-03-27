from django.urls import path

from .views import *

app_name = 'ip_manager'

urlpatterns = [
    path('', IPListView.as_view(), name='home'),

    path('add/', IPCreate.as_view(), name='add_ip'),
    path('update/<int:pk>/', IPUpdate.as_view(), name='update_ip'),
    # path('delete/<int:pk>/', IPDelete.as_view(), name='delete_ip'),
    path('<int:pk>/', IPDetailView.as_view(), name='detail_ip'),

    path('search/', IPSearchResultsView.as_view(), name='ip_search'),

]
