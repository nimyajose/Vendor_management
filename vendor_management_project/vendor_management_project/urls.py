# main_project/urls.py

from django.contrib import admin
from django.urls import path, include

from .views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view, name='base'),
    path('', include('vendor.urls')),
    path('', include('purchase_orders.urls')),
]
