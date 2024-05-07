from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import PurchaseOrder, Vendor, HistoricalPerformance

@receiver(post_save, sender=PurchaseOrder)
def calculate_on_time_delivery_rate(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        on_time_deliveries = completed_orders.filter(delivery_date__lte=timezone.now()).count()
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100
            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_quality_rating_avg(sender, instance, created, **kwargs):
    if instance.quality_rating is not None:
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_ratings = sum(order.quality_rating for order in completed_orders if order.quality_rating is not None)
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            quality_rating_avg = total_ratings / total_completed_orders
            vendor.quality_rating_avg = quality_rating_avg
            vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_average_response_time(sender, instance, created, **kwargs):
    if instance.acknowledgment_date:
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        response_times = [(order.acknowledgment_date - order.issue_date).seconds / 60 for order in completed_orders if order.acknowledgment_date]
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            average_response_time = sum(response_times) / total_completed_orders
            vendor.average_response_time = average_response_time
            vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_fulfillment_rate(sender, instance, created, **kwargs):
    vendor = instance.vendor
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    successful_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').exclude(quality_rating=None).count()
    if total_orders > 0:
        fulfillment_rate = (successful_orders / total_orders) * 100
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()
