# Generated by Django 5.0 on 2023-12-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(default='1234', max_length=1000),
        ),
    ]
