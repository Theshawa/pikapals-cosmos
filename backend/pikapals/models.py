import uuid
from django.db import models


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


class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    seat_no = models.IntegerField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.seat_no)
