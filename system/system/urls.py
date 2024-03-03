from django.contrib import admin
from django.urls import path, include
from authentication.views import RegistrationAPIView, LoginAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', RegistrationAPIView.as_view()),
    path('auth/login/', LoginAPIView.as_view()),
    path("", include("erp.urls")),
]
