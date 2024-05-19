from django.urls import path
from . import views

urlpatterns = [
    path('validate_email/', views.validate_email, name='validate_email'),
    path('validate_name/', views.validate_name, name='validate_name'),
    path('validate_date_of_birth/', views.validate_date_of_birth, name='validate_date_of_birth'),
    path('validate_phone_number/', views.validate_phone_number, name='validate_phone_number'),
    path('validate_passport/', views.validate_passport, name='validate_passport'),
    path('favorite_tickets/<int:user_id>/', views.get_favorite_tickets, name='favorite_tickets'),
    path('tickets/', views.get_tickets, name='get_tickets'),
    path('purchased_tickets/<int:user_id>/', views.get_purchased_tickets, name='get_purchased_tickets'),
]
