# Generated by Django 2.2.13 on 2021-02-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_eventbook_booking_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventbook',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='certificates'),
        ),
    ]
