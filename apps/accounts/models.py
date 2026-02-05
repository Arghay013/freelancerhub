import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    class Role(models.TextChoices):
        SELLER = "SELLER", "Seller"
        BUYER = "BUYER", "Buyer"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=Role.choices)
    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email", "role"]

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="email_token")
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
