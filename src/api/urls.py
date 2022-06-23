from .views import RouteList,BusList, TicketDetailView, TicketView, ProfileView
from django.urls import path

urlpatterns = [
    path('routes/',RouteList.as_view()),
    path('routes/<int:pk>/buses/',BusList.as_view()),
    path('user/mytickets/',TicketView.as_view()),
    path('user/profile/',ProfileView.as_view())

]
