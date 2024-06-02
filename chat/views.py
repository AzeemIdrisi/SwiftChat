from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

# Create your views here.


def home(request):
    message = request.session.get("alertMessage")
    request.session["alertMessage"] = None
    context = {
        "alertMessage": message,
    }
    return render(request, "home.html", context)


def room(request, room):

    if "user_id" not in request.session:
        return redirect("home")
    username = request.GET.get("username")
    error = request.GET.get("error")
    room_details = Room.objects.get(name=room)
    if room_details.id != request.session["user_id"]:
        return redirect("home")
    context = {
        "username": username,
        "room": room,
        "room_details": room_details,
        "error": error,
    }
    return render(request, "room.html", context)


def checkview(request):
    if not request.session.session_key:
        request.session.create()
    room = str(request.POST["room_name"]).upper().strip()
    username = request.POST["username"]
    password = request.POST["password"]

    if Room.objects.filter(name=room).exists():
        room_details = Room.objects.get(name=room)
        if room_details.password == password:
            request.session["user_id"] = room_details.id
            return redirect("room/" + room + "/?username=" + username)
        else:
            return render(
                request,
                "home.html",
                {
                    "error": 1,
                },
            )
    else:
        new_room = Room.objects.create(
            name=room, password=password, session_key=request.session.session_key
        )
        new_room.save()
        request.session["user_id"] = new_room.id
        return redirect("room/" + room + "/?username=" + username)


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

    # If room had already been deleted
    if not Room.objects.filter(name=room).exists():
        request.session["alertMessage"] = f"{room}"
        return redirect("home")
    else:
        # If room still exists
        room_details = Room.objects.get(name=room)
        # checking for creator
        if room_details.session_key == request.session.session_key:
            room_details.delete()
            request.session["alertMessage"] = f"{room}"
            request.session["user_id"] = None
            return redirect("home")
        else:
            url = reverse("room", kwargs={"room": room})
            return redirect(url + "?error=1")
