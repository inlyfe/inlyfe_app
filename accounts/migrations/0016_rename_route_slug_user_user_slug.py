# Generated by Django 4.2.2 on 2023-06-16 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_user_route_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='route_slug',
            new_name='user_slug',
        ),
    ]
