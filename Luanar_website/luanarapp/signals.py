from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Newsletter, Subscriber

@receiver(post_save, sender=Newsletter)
def send_newsletter_to_subscribers(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            email = EmailMessage(
                instance.title,
                'Please find the latest newsletter attached. LUANAR a University with Endless Possibilities',
                settings.EMAIL_HOST_USER,
                [subscriber.email]
            )
            email.attach_file(instance.pdf.path)
            email.send(fail_silently=False)
