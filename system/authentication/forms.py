from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('director', 'Директор'),
        ('worker', 'Рабочий'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, help_text='Выберите вашу должность')
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name','role' ,'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']