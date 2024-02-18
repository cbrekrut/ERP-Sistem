from django.contrib import admin
from .models import CustomUser,Factory,CustomUserManager,Task

admin.site.register(Task)
admin.site.register(CustomUser)
admin.site.register(Factory)
