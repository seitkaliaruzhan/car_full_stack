from rest_framework import viewsets
from cars.models import Car, Owner
from cars.serializers import CarSerializer, OwnerSerializer
from rest_framework.permissions import IsAuthenticated

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Car.objects.all()
        brand = self.request.query_params.get('brand')
        color = self.request.query_params.get('color')
        
        if brand:
            queryset = queryset.filter(brand__iexact=brand)
        if color:
            queryset = queryset.filter(color__iexact=color)
            
        return queryset


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
