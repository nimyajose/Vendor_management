from django.urls import path
from .views import PurchaseOrderAcknowledge, PurchaseOrderCreate, PurchaseOrderList, PurchaseOrderRetrieveUpdateDestroy

urlpatterns = [
    path('api/purchase_orders/', PurchaseOrderList.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase-order-detail'),
    path('api/purchase_orders/create/', PurchaseOrderCreate.as_view(), name='purchase-order-create'),
    path('api/purchase_orders/<int:pk>/acknowledge/', PurchaseOrderAcknowledge.as_view(),
         name='purchase-order-acknowledge'),
]
