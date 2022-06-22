from bookings.models import Ticket,Bus,Route
from bookings.serializers import RouteSerializer,TicketSerializer,BusSerializer
from rest_framework import generics

# Create your views here.

class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class BusList(generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
