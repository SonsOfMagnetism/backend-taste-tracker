from .models import Restaurant
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RestaurantSerializer

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]