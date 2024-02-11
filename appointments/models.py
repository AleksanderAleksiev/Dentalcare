from django.db import models
from user.models import UserAccount


class Appointment(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    creation_date_time = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='patient', null=True, blank=True)
    dentist = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='dentist')
    is_all_day = models.BooleanField(default=False, null=True, blank=True)
    recurrence_rule = models.CharField(max_length=50, null=True, blank=True)
    excluded_dates = models.CharField(max_length=400, null=True, blank=True)


    def __str__(self) -> str:
        return f'{self.title}, occurs from {self.start_date} until {self.end_date}'