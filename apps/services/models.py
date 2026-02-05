from django.db import models
from django.conf import settings

class Service(models.Model):
    class Category(models.TextChoices):
        GRAPHIC_DESIGN = "graphic_design", "Graphic Design"
        WRITING = "writing", "Writing"
        PROGRAMMING = "programming", "Programming"
        OTHER = "other", "Other"

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=Category.choices)
    delivery_time_days = models.PositiveIntegerField()
    requirements = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
