from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Reserva, Cliente, Habitacion, Hotel
from .serializers import ReservaSerializer, ClienteSerializer, HabitacionSerializer, HotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class CustomAPIView(APIView):
    def get(self, request):
        # Lógica de la vista personalizada
        return Response({"message": "Custom API View"})