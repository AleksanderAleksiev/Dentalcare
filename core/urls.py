from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/appointments/', include('appointments.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('auth/user/', include('user.urls')),
    path('admin/', admin.site.urls),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)