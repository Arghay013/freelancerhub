from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.services.models import Service
from apps.orders.models import Order

User = get_user_model()

class Command(BaseCommand):
    help = "Seed demo users + services + an order"

    def handle(self, *args, **kwargs):
        seller, _ = User.objects.get_or_create(
            username="seller1",
            defaults={"email":"seller1@example.com","role":"SELLER","is_verified":True},
        )
        seller.set_password("Seller@12345")
        seller.is_verified = True
        seller.save()

        buyer, _ = User.objects.get_or_create(
            username="buyer1",
            defaults={"email":"buyer1@example.com","role":"BUYER","is_verified":True},
        )
        buyer.set_password("Buyer@12345")
        buyer.is_verified = True
        buyer.save()

        s1, _ = Service.objects.get_or_create(
            seller=seller,
            title="Logo Design",
            defaults={
                "description":"Professional logo design with 3 concepts.",
                "price":50,
                "category":"graphic_design",
                "delivery_time_days":3,
                "requirements":"Company name, colors, style preference",
            },
        )

        if not Order.objects.filter(buyer=buyer, service=s1).exists():
            Order.objects.create(buyer=buyer, service=s1, note="Need a modern logo")

        self.stdout.write(self.style.SUCCESS("Demo data created"))
        self.stdout.write("Seller: seller1@example.com / Seller@12345")
        self.stdout.write("Buyer : buyer1@example.com / Buyer@12345")
