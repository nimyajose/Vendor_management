# vendors/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from purchase_orders .models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        vendor.on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
        vendor.save()
