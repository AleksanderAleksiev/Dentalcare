
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'title', 'description', 'start_date', 'end_date', 'creation_date_time', 'patient', 'dentist', 'is_all_day', 'recurrence_rule', 'excluded_dates')