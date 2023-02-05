from rest_framework import serializers
from .models import Event, Booking, Room

DATE_INPUT_FORMATS = ["%d-%m-%Y", "%Y-%m-%d"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "name", "capacity")


class EventSerializer(serializers.ModelSerializer):
    room_name = serializers.ReadOnlyField(source='room.name')

    class Meta:
        model = Event
        fields = ("id", "name", "type", "start_date", "end_date", "room_name")


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("created_by", "event", "date")


class BookingPayloadSerializer(serializers.Serializer):
    created_by = serializers.IntegerField(required=True)
    event = serializers.IntegerField(required=True)
    date = serializers.DateField(input_formats=DATE_INPUT_FORMATS, required=True)

    class Meta:
        fields = (
            "created_by",
            "event",
            "date",
        )
