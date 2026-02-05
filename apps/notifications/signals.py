from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.orders.models import Order
from .models import Notification

@receiver(post_save, sender=Order)
def order_notification(sender, instance: Order, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.buyer, message=f"Your order #{instance.id} was placed (status: {instance.status}).")
        Notification.objects.create(user=instance.service.seller, message=f"New order #{instance.id} for '{instance.service.title}'.")
    else:
        Notification.objects.create(user=instance.buyer, message=f"Order #{instance.id} status updated to {instance.status}.")
        Notification.objects.create(user=instance.service.seller, message=f"Order #{instance.id} status updated to {instance.status}.")
