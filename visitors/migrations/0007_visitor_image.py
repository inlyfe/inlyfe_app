# Generated by Django 4.2.2 on 2023-06-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0006_visitor_date_visited_alter_visitor_in_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='image',
            field=models.ImageField(null=True, upload_to='visitors/'),
        ),
    ]