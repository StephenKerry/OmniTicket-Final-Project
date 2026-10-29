import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .tasks import send_queue_email


def home(request):
    sent = False
    if request.method == "POST":
        text = request.POST.get("message", "")
        send_queue_email.delay(text)  # puts the message on the Redis queue
        sent = True
    return render(request, "queuedemo/home.html", {"sent": sent})


@csrf_exempt
def api_message(request):
    data = json.loads(request.body)
    text = data.get("message", "")
    send_queue_email.delay(text)
    return JsonResponse({"status": "queued"})