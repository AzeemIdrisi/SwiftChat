# Generated by Django 5.0.2 on 2024-02-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='session_key',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
