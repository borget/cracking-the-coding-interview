from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.permissions import BasePermission, IsAdminUser as IsBusinessUser, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from .serializers import EventSerializer, BookingSerializer, RoomSerializer
from .models import Event, Booking, Room, EventType
from .services import BookingService


class CustomerAccess(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsBusinessUser]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if Event.objects.filter(room=instance):
            return Response({"error": "The room cannot be deleted, it has ongoing events."},
                            status=status.HTTP_409_CONFLICT)

        return super().destroy(request, *args, **kwargs)


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsBusinessUser | CustomerAccess]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user

        if not user.is_superuser:
            return queryset.filter(type=EventType.PUBLIC)

        return queryset


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    service = BookingService()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.service.validate_booking_rules(request.data)

        self.perform_create(serializer)

        self.service.decrease_room_space(request.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        self.service.increase_room_space(instance.event.room)

        return Response(status=status.HTTP_204_NO_CONTENT)
