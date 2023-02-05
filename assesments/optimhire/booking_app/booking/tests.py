from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
import factory
import pytest

from booking.models import Booking, EventType, Event, Room


@pytest.fixture
def user(db):
    user = User.objects.create(
        username="alberto", is_staff=False, is_superuser=False, is_active=True
    )
    user.set_password("test")
    user.save()
    return user


@pytest.fixture
def admin_client(user, admin_client):
    admin_client.force_login(user)
    return admin_client


def booking_url():
    return reverse("booking")


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "booking.Room"

    name = "My Room"
    capacity = 100
    avail_space = None


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "booking.Event"

    name = "Optimhire Event"
    type = EventType.PUBLIC
    start_date = factory.LazyFunction(timezone.now)
    end_date = factory.LazyFunction(lambda: timezone.now() + timezone.timedelta(hours=2))
    room = factory.SubFactory("booking.tests.RoomFactory")


def test_book_a_space_for_an_event(admin_client):
    EventFactory.create()
    event = Event.objects.filter(name="Optimhire Event").first()
    user = User.objects.filter(username="alberto").first()

    payload = {
        "created_by": user.id,
        "event": event.id,
        "date": "2023-01-25"
    }

    response = admin_client.post(booking_url(), data=payload)

    assert response.status_code == 201
    assert Booking.objects.count() == 1

    booking = Booking.objects.first()
    assert booking.event == payload["event"]

    room = Room.objects.filter(id=event.room.id).first()

    assert room.avail_space == room.capacity - 1


def test_should_not_book_a_space_if_event_has_no_availability(admin_client):
    room = RoomFactory.create(capacity=0)
    EventFactory.create(room=room)
    event = Event.objects.filter(name="Optimhire Event").first()
    user = User.objects.filter(username="alberto").first()

    payload = {
        "created_by": user.id,
        "event": event.id,
        "date": "2023-01-25"
    }

    response = admin_client.post(booking_url(), data=payload)

    assert response.status_code == 400
    assert Booking.objects.count() == 0
