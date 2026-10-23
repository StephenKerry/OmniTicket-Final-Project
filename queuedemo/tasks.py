from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_queue_email(message):
    send_mail(
        subject="Someone put a message on the queue",
        message=f"The message was: {message}",
        from_email="stephenkerry2013@gmail.com",
        recipient_list=["20106900@setu.ie"],
    )