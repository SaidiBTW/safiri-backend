from .views import RouteList,BusList, TicketDetailView
from django.urls import path

urlpatterns = [
    path('routes/',RouteList.as_view()),
    path('routes/<int:pk>/buses/',BusList.as_view()),
    path('tickets/<int:pk>',TicketDetailView.as_view()),

]
