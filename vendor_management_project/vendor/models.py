from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            # Add more indexes as needed
        ]

    def __str__(self):
        return self.name

    # Add optimized calculation logic
    def calculate_on_time_delivery_rate(self):
        total_completed_orders = self.purchaseorder_set.filter(status='completed').count()
        if total_completed_orders > 0:
            on_time_deliveries = self.purchaseorder_set.filter(status='completed', delivery_date__lte=models.F('issue_date')).count()
            return (on_time_deliveries / total_completed_orders) * 100
        else:
            return 0

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"



