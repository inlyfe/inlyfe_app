# Generated by Django 4.2.2 on 2023-06-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_services', '0005_passenger_created_at_payment_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_slug',
            field=models.SlugField(null=True),
        ),
    ]