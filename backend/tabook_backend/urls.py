"""
URL configuration for tabook_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservations.views import (
    ReservationViewSet,
    admin_dashboard,
    confirm_reservation,
    reset_reservations,
    delete_reservation,  # Importa la funzione per eliminare le prenotazioni
)

# Configura il router per l'API REST
router = DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='reservation')

# Definizione degli URL
urlpatterns = [
    path('admin/', admin.site.urls),  # Accesso al pannello di amministrazione Django
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),  # URL per la dashboard dell'admin
    path('api/confirm-reservation/<int:reservation_id>/', confirm_reservation, name='confirm_reservation'),  # URL per confermare una prenotazione
    path('api/', include(router.urls)),  # Include gli endpoint dell'API REST
    path('api/reset-reservations/', reset_reservations, name='reset_reservations'),
    path('api/delete-reservation/<int:pk>/', delete_reservation, name='delete_reservation'),  # Endpoint per eliminare una prenotazione
]
