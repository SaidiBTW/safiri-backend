from rest_framework import generics
from .models import Bus,Ticket,Route
from .serializers import BusSerializer,TicketSerializer,RouteSerializer

# Create your views here.
class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class  TicketView(generics.GenericAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class BusSerializer(generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer