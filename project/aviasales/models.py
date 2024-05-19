from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import validate_email
import re
def validate_phone_number(value):
    pattern = r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$'
    if not re.match(pattern, value):
        raise ValidationError('Неверный формат номера телефона')

class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=16, validators=[validate_phone_number])
    email = models.CharField(max_length=255, validators=[validate_email])
    settings = models.ForeignKey('Settings', on_delete=models.CASCADE, related_name='user_related')

class Settings(models.Model):
    id = models.AutoField(primary_key=True)
    interface_language = models.CharField(max_length=25)
    city_of_residence = models.CharField(max_length=40)
    currency = models.CharField(max_length=4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_settings')

class Documentation(models.Model):
    id = models.AutoField(primary_key=True)
    citizenship = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    passport_series = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Tickets(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    departure_location = models.CharField(max_length=50)
    arrival_location = models.CharField(max_length=50)
    flight = models.CharField(max_length=50)
    airplane = models.CharField(max_length=50)
    sent_in_plane = models.CharField(max_length=50)
    number_of_passengers = models.IntegerField()

class PurchasedTickets(models.Model):
    id = models.AutoField(primary_key=True)
    time_of_creation = models.DateTimeField()
    payment_type = models.CharField(max_length=50)
    payment_state = models.CharField(max_length=50)
    payment_time = models.DateTimeField()
    status = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tickets = models.ForeignKey(Tickets, on_delete=models.CASCADE)

class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    tickets = models.ManyToManyField(Tickets)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
