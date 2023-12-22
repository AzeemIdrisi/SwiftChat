from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.CharField(max_length=100, default="Anonymous")
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user + " : " + self.text
