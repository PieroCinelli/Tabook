from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    num_people = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time} ({self.num_people} persone)"
