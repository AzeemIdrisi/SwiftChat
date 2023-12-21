from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    return render(request, "home.html")


def room(request, room):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    context = {
        "username": username,
        "room": room,
        "room_details": room_details,
    }
    return render(request, "room.html", context)


def checkview(request):
    room = request.POST["room_name"]
    username = request.POST["username"]

    if Room.objects.filter(name=room).exists():
        return redirect(room + "/?username=" + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect(room + "/?username=" + username)


def send(request):
    message = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]
    room = Room.objects.get(id=room_id)
    new_message = Message.objects.create(text=message, user=username, room=room)
    new_message.save()
    return HttpResponse("Message sent.")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details)
    return JsonResponse({"messages": list(messages.values())})
