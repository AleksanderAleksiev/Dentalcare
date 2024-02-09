from django.urls import path
from .views import get_all_appointments, get_user_appointments_by_date_range, create_appointment, appointment_detail

urlpatterns = [
    path('all', get_all_appointments),
    path('user_appointments', get_user_appointments_by_date_range),
    path('create', create_appointment),
    path('<int:id>', appointment_detail),
]