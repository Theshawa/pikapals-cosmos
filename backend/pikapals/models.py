import uuid
from typing import List, Tuple

from django.contrib.auth.models import User
from django.db import models
from enum import Enum

from django.db.models import ForeignKey


class Port(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def to_data(self):
        return {
            "id": str(self.id),
            "name": self.name
        }


class ServiceProvider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def to_data(self):
        return {
            "id": str(self.id),
            "name": self.name
        }


class Voyage(models.Model):
    voyage_no = models.CharField(max_length=100, primary_key=True)
    start = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="start_voyages")
    destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="destination_voyages")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    min_ticket_price = models.IntegerField()
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)

    def __str__(self):
        return self.voyage_no

    def to_data(self):
        return {
            "voyage_no": self.voyage_no,
            "start": self.start.to_data(),
            "destination": self.destination.to_data(),
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "min_ticket_price": self.min_ticket_price,
            "service_provider": self.service_provider.to_data(),
        }

    def create_seats(self, seats: List[Tuple['SeatClass', int, int]]):
        for (index, seat) in enumerate(seats):
            Seat(voyage=self, seat_class=seat[0], seat_no=seat[1], price=seat[2], available=True).save()
        self.save()


class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    seat_no = models.IntegerField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    seat_class = models.CharField(max_length=100) # SeatClass Enum
    booked_by = ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="booked_seats")

    def __str__(self):
        return str(self.seat_no)

    def to_data(self):
        return {
            "id": str(self.id),
            "voyage": self.voyage.voyage_no,
            "seat_no": self.seat_no,
            "price": self.price,
            "available": self.available,
            "seat_class": self.seat_class,
        }


class SeatClass(Enum):
    ECONOMY = "ECONOMY"
    BUSINESS = "BUSINESS"
    FIRST = "FIRST"