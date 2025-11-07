from django.db import models

# Create your models here.

class Hotel(models.Model):
    description = models.TextField(default='room description', verbose_name='room description')
    price = models.IntegerField(default=100, verbose_name='price per night')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='date of creation')

    def __str__(self):
        return f'Hotel {self.id} - {self.description[:20]}'

class Reservations(models.Model):
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    hotel_id = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='reservations',
        verbose_name='hotel'
    )

    def __str__(self):
        return f'Reservation {self.id} for Hotel {self.hotel_id}'