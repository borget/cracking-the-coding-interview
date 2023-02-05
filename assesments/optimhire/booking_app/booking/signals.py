from django.db.models.signals import pre_delete
from django.dispatch import receiver

from booking.models import Event, Room


@receiver(pre_delete, sender=Room)
def delete_room(sender, instance, **kwargs):
    if Event.objects.filter(room=instance):
        raise Exception("Room has ongoing events.")
    instance.delete()
