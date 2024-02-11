from django.urls import path
from .views import RegisterView, RetrieveUserView, get_all_dentists, get_user_detail



urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view()),
    path('dentists/all', get_all_dentists),
    path('<int:id>', get_user_detail),
]

