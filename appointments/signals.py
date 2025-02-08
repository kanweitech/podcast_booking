from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Appointment

@receiver(post_save, sender=Appointment)
def handle_appointment_notification(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    subject = f'Appointment {action.capitalize()}'
    message = f'''Your appointment at {instance.studio.name} has been {action}.
    Details:
    - Start Time: {instance.start_time}
    - End Time: {instance.end_time}
    - Status: {instance.status}'''
    send_mail(subject, message, None, [instance.user.email])

@receiver(pre_delete, sender=Appointment)
def handle_appointment_deletion(sender, instance, **kwargs):
    subject = 'Appointment Cancelled'
    message = f'Your appointment at {instance.studio.name} on {instance.start_time} has been cancelled.'
    send_mail(subject, message, None, [instance.user.email])