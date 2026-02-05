from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import EmailVerificationToken

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username","email","role","is_verified","is_staff")
    list_filter = ("role","is_verified","is_staff")
    search_fields = ("username","email")

@admin.register(EmailVerificationToken)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = ("user","token","created_at")
