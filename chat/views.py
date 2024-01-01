from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

# Create your views here.


def home(request):
    message = request.session.get("message")
    request.session["message"] = None
    context = {
        "message": message,
    }
    return render(request, "home.html", context)


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
    room = str(request.POST["room_name"]).upper().strip()
    username = request.POST["username"]
    password = request.POST["password"]

    if Room.objects.filter(name=room).exists():
        room_details = Room.objects.get(name=room)
        if room_details.password == password:
            return redirect(room + "/?username=" + username)
        else:
            return render(
                request,
                "home.html",
                {
                    "message": "Wrong Password or Room ID not available",
                },
            )
    else:
        new_room = Room.objects.create(name=room, password=password)
        new_room.save()
        return redirect(room + "/?username=" + username)


def send(request):
    message = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]
    room = Room.objects.get(id=room_id)
    if len(username) == 0:
        username = "Anonymous"
    if len(message) > 0:
        new_message = Message.objects.create(text=message, user=username, room=room)
        new_message.save()
    return HttpResponse("Message sent.")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details)
    return JsonResponse({"messages": list(messages.values())})


def delete(request, room):
    room_details = Room.objects.get(name=room)
    room_details.delete()
    request.session["message"] = f"Room [{room}] deleted successfully."

    return redirect("home")
