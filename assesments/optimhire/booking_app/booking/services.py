from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from booking.models import Booking, Event, EventType, Room


class BookingService:
    def validate_booking_rules(self, booking_data):
        event = get_object_or_404(Event, id=booking_data["event"])

        self._is_event_private(event)
        self._allow_only_one_per_day(booking_data)
        self._can_book_a_space(event)

    def _can_book_a_space(self, event):
        room = event.room
        if event.type == EventType.PUBLIC and not room.has_availability:
            raise ValidationError(detail="There are no space available for this event.")

    def _is_event_private(self, event):
        if event.type == EventType.PRIVATE:
            raise ValidationError(detail="This event is private, you cannot schedule an event at this time.")

    def _allow_only_one_per_day(self, booking_data):
        if Booking.objects.filter(date=booking_data["date"]):
            raise ValidationError(detail="Only one event per day is allowed.")

    def increase_room_space(self, room):
        room.avail_space += 1
        room.save()

    def decrease_room_space(self, booking_data):
        event = get_object_or_404(Event, id=booking_data["event"])
        event.room.avail_space -= 1
        event.room.save()
