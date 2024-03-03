from django.urls import path
from . import views


urlpatterns = [
    path('', views.booking, name='booking'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]
