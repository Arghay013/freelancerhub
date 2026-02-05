# Freelancer Platform API (Django + DRF)

This project uses a **current Django 5.x** style and conventions:
- Django 5.x + DRF
- Custom user model with roles (SELLER/BUYER)
- Email verification required for login (JWT)
- Services + filtering/sorting
- Orders + status tracking
- Notifications
- Reviews after completion
- Dashboards
- OpenAPI/Swagger (drf-spectacular)

## Run (Windows CMD)
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

copy .env.example .env

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py seed_demo

python manage.py runserver
```

## Swagger
- http://127.0.0.1:8000/api/docs/

## Demo users (after seed_demo)
- Seller: seller1@example.com / Seller@12345
- Buyer:  buyer1@example.com / Buyer@12345

## IMPORTANT (fix for error)
This repo includes `apps/__init__.py` so Django detects all local apps and creates migrations correctly.
