from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    num_people = models.PositiveIntegerField()
    max_people = models.PositiveIntegerField(default=4)  # Limite massimo per prenotazione
    group_id = models.CharField(max_length=100, null=True, blank=True)  # ID del gruppo per raggruppare le prenotazioni
    is_confirmed = models.BooleanField(default=False)  # Per tracciare la conferma
    phone_number = models.CharField(max_length=15, default='+390000000000')  # Valore predefinito
    is_confirmed = models.BooleanField(default=False)
    available_times = models.JSONField(default=list)  # Lista di orari disponibili (esempio: ["12:00", "14:00", "16:00"])
    
    # Campi aggiuntivi per suddivisione storica
    month = models.IntegerField(default=1)
    year = models.IntegerField(default=2025)

    def save(self, *args, **kwargs):
        # Imposta automaticamente il mese e l'anno dalla data
        if self.date:
            self.month = self.date.month
            self.year = self.date.year
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.date} {self.time} ({self.num_people} persone)"
