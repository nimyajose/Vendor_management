from rest_framework import generics
from .models import Vendor
from rest_framework.response import Response
from .serializers import VendorSerializer
from .serializers import VendorPerformanceSerializer
class VendorCreate(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorList(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceRetrieve(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)