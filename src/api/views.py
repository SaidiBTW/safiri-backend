from bookings.permissions import IsOwner
from bookings.models import Ticket,Bus,Route
from users.models import Member
from bookings.serializers import RouteSerializer,TicketSerializer,BusSerializer
from users.serializers import MemberSerializer
from rest_framework import generics

# Create your views here.

#get a list of routes
class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

#get list of buses
class BusList(generics.ListAPIView):
    serializer_class = BusSerializer

    def get_queryset(self):
        return Bus.objects.all()
    

#get your ticket
class TicketDetailView(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(traveller = user.id)
    
    

#create your ticket
class  TicketCreationView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(traveller = user)

#get your profile
class ProfileView(generics.ListAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        user = self.request.user
        return Member.objects.filter(username = user.username)
    
