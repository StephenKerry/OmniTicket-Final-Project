from django.shortcuts import render
from .tasks import send_queue_email


def home(request):
    sent = False
    if request.method == "POST":
        text = request.POST.get("message", "")
        send_queue_email.delay(text)  # puts the message on the Redis queue
        sent = True
    return render(request, "queuedemo/home.html", {"sent": sent})