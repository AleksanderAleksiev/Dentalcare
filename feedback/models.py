from django.db import models
from user.models import UserAccount


class Feedback(models.Model):
    text=models.CharField(max_length=500)
    created_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='created_by')
    creation_date_time = models.DateTimeField(auto_now_add=True)
    dentist = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='commented_dentist')

    
    def __str__(self) -> str:
        return f'Feedback: {self.text}, about {self.dentist}, created by {self.created_by}, {self.creation_date_time}'