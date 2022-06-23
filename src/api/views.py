from bookings.permissions import IsOwner
from bookings.models import Ticket,Bus,Route
from users.models import Member
from bookings.serializers import RouteSerializer,TicketSerializer,BusSerializer
from users.serializers import MemberSerializer
from rest_framework import generics

# Create your views here.

class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class BusList(generics.ListAPIView):
    serializer_class = BusSerializer

    def get_queryset(self):
        return Bus.objects.all()
    

class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class  TicketView(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(traveller = user)

class ProfileView(generics.ListAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        user = self.request.user
        return Member.objects.filter(username = user.username)
    
