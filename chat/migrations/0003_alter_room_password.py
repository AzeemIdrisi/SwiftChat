# Generated by Django 5.0 on 2023-12-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='password',
            field=models.CharField(max_length=1000),
        ),
    ]