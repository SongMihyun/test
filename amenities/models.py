# type: ignore

from django.db import models

from accommodations.models import Accommodation
from rooms.models import Room


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    is_custom = models.BooleanField(default=False)


class AccommodationAmenity(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    custom_value = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ("accommodation", "amenity")


class Option(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    is_custom = models.BooleanField(default=False)


class RoomOption(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    custom_value = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ("room", "option")
