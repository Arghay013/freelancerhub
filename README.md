# FreelancerHub – Freelancer Platform Backend API

This is a **backend-only REST API** for a Freelancer Platform where **Sellers** can offer digital services and **Buyers** can place orders.  
The project is built using **Django 5.x** and **Django REST Framework (DRF)** following modern best practices.

---

## 🚀 Key Features

### 🔐 User Authentication
- Custom user model
- Two roles: **Seller** and **Buyer**
- JWT-based authentication (SimpleJWT)
- Email verification required before login

### 🛠 Services
- Sellers can create and manage services
- Service details: title, description, price, category, delivery time
- Buyers can view services
- Filtering by category
- Sorting by price (low → high, high → low)

### 📦 Orders
- Buyers can place orders for services
- Order status tracking:
  - Pending
  - In Progress
  - Completed
- Sellers can manage orders for their services

### ⭐ Reviews & Ratings
- Buyers can leave reviews after order completion
- Sellers can view ratings and feedback

### 📊 Dashboards
- Seller dashboard: services, orders, earnings
- Buyer dashboard: order history

### 📄 API Documentation
- OpenAPI / Swagger documentation using **drf-spectacular**

---

## 🧰 Tech Stack

- Python
- Django 5.x
- Django REST Framework
- JWT Authentication (djangorestframework-simplejwt)
- PostgreSQL (Supabase)
- Swagger / OpenAPI (drf-spectacular)
- Deployed on **Vercel**

---

## 🌐 Live API Documentation (Swagger)

https://freelancerhub-mauve.vercel.app/api/docs/


All API endpoints can be tested directly from Swagger using JWT authentication.

---

## 🔐 Authentication Guide (Swagger)

1. Use `POST /api/auth/token/` to login and obtain JWT tokens  
2. Copy the **access token**
3. Click **Authorize** in Swagger
4. Paste the token as:
Bearer <access_token>

5. You can now access protected endpoints

---

## 👤 Test Credentials

### Admin
Username: adp
Password: 1234

### Seller
Username: seller1
Password: Seller@12345

### Buyer
Username: buyer1
Password: Buyer@12345

---

## ⚙️ Run Locally (Windows CMD)

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
Swagger (local):
http://127.0.0.1:8000/api/docs/
🛫 Deployment

Backend deployed on Vercel using serverless functions

PostgreSQL database hosted on Supabase

Static files are not served on Vercel

Swagger UI is used as the primary interface for API testing