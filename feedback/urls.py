from django.urls import path
from .views import get_feedback_all, get_user_feedback, get_dentist_feedback, create_feedback, feedback_detail

urlpatterns = [
    path('all', get_feedback_all),
    path('my_feedback', get_user_feedback),
    path('dentist/<int:id>', get_dentist_feedback),
    path('create', create_feedback),
    path('<int:id>', feedback_detail),
]