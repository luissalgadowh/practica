from __future__ import absolute_import
from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail

@shared_task
def add(nombre, apellido, correo):

    mensaje = f"Se agrego la persona {nombre} {apellido} con el correo {correo}"

    send_mail(
        'Hola Luis, se ha creado un nuevo usuario',
        mensaje,
        settings.EMAIL_HOST_USER,
        ['luissalgado9@hotmail.com'],
        fail_silently=False)
    
    return mensaje
