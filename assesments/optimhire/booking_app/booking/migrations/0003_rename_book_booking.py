# Generated by Django 4.1.5 on 2023-01-25 02:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("booking", "0002_book"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Book",
            new_name="Booking",
        ),
    ]
