from django.contrib.auth.models import User
from django.db import models

from rest_framework.exceptions import ValidationError


class EventType(models.TextChoices):
    PUBLIC = "public",
    PRIVATE = "private"


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    avail_space = models.PositiveIntegerField(null=True, blank=True)

    @property
    def has_availability(self) -> bool:
        return self.avail_space > 0

    def save(self, *args, **kwargs):
        if self.avail_space is None:
            self.avail_space = self.capacity

        if self.avail_space > self.capacity:
            raise ValidationError(detail="Room space availability cannot be greater than the max capacity.")

        return super().save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=15,
        choices=EventType.choices,
        default=EventType.PRIVATE,
    )
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Booking(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
