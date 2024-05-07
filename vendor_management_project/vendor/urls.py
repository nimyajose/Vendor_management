from django.urls import path
from .views import VendorCreate, VendorList, VendorRetrieveUpdateDestroy, VendorPerformanceRetrieve

urlpatterns = [
    path('api/vendors/', VendorList.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroy.as_view(), name='vendor-detail'),
    path('api/vendors/create/', VendorCreate.as_view(), name='vendor-create'),
    path('api/vendors/<int:pk>/performance/', VendorPerformanceRetrieve.as_view(), name='vendor-performance'),
]
