from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'num_people', 'available_times']  # Aggiungi il campo `available_times`
    
    # Aggiungi un campo custom per i selettori di orari
    available_times = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}),
        required=False,
        help_text="Inserisci gli orari disponibili separati da una virgola (es. 12:00, 14:00)"
    )