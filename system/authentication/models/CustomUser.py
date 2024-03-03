from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .CustomUserManager import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    ROLE_CHOICES = (
        ('director', 'Директор'),
        ('worker', 'Рабочий'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='worker')
    subordinates = models.ManyToManyField('self', symmetrical=False, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    def __str__(self):
        return self.email

    class Meta:
        permissions = (("can_view_custom_user", "Can view custom user"),)
        swappable = "AUTH_USER_MODEL"
