from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "price", "delivery_time_days", "seller", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("title", "description")
