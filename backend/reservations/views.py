from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer
from twilio.rest import Client
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.db import models

# API ViewSet per gestire le prenotazioni tramite l'API REST
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        """Crea una nuova prenotazione e verifica il limite di posti."""
        date = request.data.get('date')
        time = request.data.get('time')
        num_people = int(request.data.get('num_people', 0))

        # Controlla se i dati richiesti sono completi
        if not date or not time or num_people <= 0:
            return HttpResponseBadRequest("Dati della prenotazione mancanti o non validi.")

        # Calcola il numero totale di persone prenotate per la stessa data e orario
        total_reserved = Reservation.objects.filter(date=date, time=time).aggregate(
            models.Sum('num_people')
        )['num_people__sum'] or 0

        # Limite di persone per fascia oraria
        max_people = 20  # Supponiamo ci siano 20 posti disponibili

        if total_reserved + num_people > max_people:
            return HttpResponseBadRequest("Limite di posti raggiunto per questa data e orario.")

        # Crea la prenotazione se tutto è valido
        return super().create(request, *args, **kwargs)

# Funzione per inviare un SMS di conferma tramite Twilio
def send_sms_confirmation(to_number, reservation_details):
    """Invia un SMS di conferma utilizzando Twilio."""
    from twilio.base.exceptions import TwilioRestException
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message_body = (
        f"Ciao {reservation_details['name']}! La tua prenotazione è stata confermata.\n"
        f"Dettagli:\n"
        f"Data: {reservation_details['date']}\n"
        f"Orario: {reservation_details['time']}\n"
        f"Numero di persone: {reservation_details['num_people']}\n"
        f"Grazie per aver scelto il nostro servizio!"
    )

    try:
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_number
        )
        return message.sid  # Ritorna il SID per confermare l'invio
    except TwilioRestException as e:
        print(f"Errore Twilio: {e}")
        return None
    except Exception as ex:
        print(f"Errore generico: {ex}")
        return None

# Vista per la dashboard admin
def admin_dashboard(request):
    """Visualizza la dashboard admin con statistiche e prenotazioni."""
    total_tables = 20  # Supponiamo ci siano 20 tavoli in totale
    reservations = Reservation.objects.all()
    total_people = reservations.aggregate(models.Sum('num_people'))['num_people__sum'] or 0
    booked_tables = reservations.count()
    available_tables = max(0, total_tables - booked_tables)

    context = {
        "reservations": reservations,
        "total_tables": total_tables,
        "booked_tables": booked_tables,
        "available_tables": available_tables,
        "total_people": total_people,
    }
    return render(request, "admin_dashboard.html", context)

# Vista per confermare una prenotazione
def confirm_reservation(request, reservation_id):
    """Conferma una prenotazione e invia un SMS al cliente."""
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.is_confirmed = True  # Imposta come confermata
    reservation.save()

    reservation_details = {
        "name": reservation.name,
        "date": reservation.date,
        "time": reservation.time,
        "num_people": reservation.num_people,
    }

    sms_status = send_sms_confirmation(reservation.phone_number, reservation_details)

    if not sms_status:
        return JsonResponse({"error": "Errore durante l'invio del messaggio SMS."}, status=500)

    return redirect("admin_dashboard")



def reset_reservations(request):
    if request.method == "DELETE":
        Reservation.objects.all().delete()
        return JsonResponse({"message": "Database delle prenotazioni resettato con successo."})
    return JsonResponse({"error": "Metodo non consentito."}, status=405) 

# Vista per eliminare una prenotazione
@api_view(['DELETE'])
def delete_reservation(request, pk):
    """
    Elimina una prenotazione specificata dal suo ID (pk).
    """
    try:
        # Recupera la prenotazione
        reservation = Reservation.objects.get(pk=pk)

        # Elimina la prenotazione
        reservation.delete()
        return Response({"message": "Prenotazione eliminata con successo."}, status=status.HTTP_200_OK)

    except Reservation.DoesNotExist:
        return Response({"error": "Prenotazione non trovata."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Gestione di altri errori
        return Response({"error": "Si è verificato un errore durante l'eliminazione della prenotazione.", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)