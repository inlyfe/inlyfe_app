# Generated by Django 4.2.2 on 2023-06-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_services', '0004_rename_group_tripgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='seat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tripgroup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
