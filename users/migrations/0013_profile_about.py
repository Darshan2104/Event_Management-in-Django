# Generated by Django 2.2.13 on 2021-03-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_profile_numberofupdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(default='Hello'),
        ),
    ]