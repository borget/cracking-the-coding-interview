# Generated by Django 4.1.5 on 2023-01-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_rename_book_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="avail_space",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]