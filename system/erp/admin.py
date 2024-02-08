from django.contrib import admin
from .models import CustomUser,Factory,CustomUserManager


admin.site.register(CustomUser)
admin.site.register(Factory)
