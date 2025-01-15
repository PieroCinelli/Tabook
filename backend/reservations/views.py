from django.shortcuts import render
from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer

# API ViewSet per gestire le prenotazioni tramite l'API REST
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# Vista per la dashboard admin
def admin_dashboard(request):
    # Calcolo delle statistiche
    total_tables = 20  # Supponiamo ci siano 20 tavoli in totale
    reservations = Reservation.objects.all()
    booked_tables = reservations.count()
    available_tables = total_tables - booked_tables

    # Passa le informazioni al template
    context = {
        "reservations": reservations,
        "total_tables": total_tables,
        "booked_tables": booked_tables,
        "available_tables": available_tables,
    }
    return render(request, "admin_dashboard.html", context)
