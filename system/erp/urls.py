from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("erp/", views.erp, name='erp'),
    path("customers/", views.customers, name='customers'),
    path('save_task/<int:user_id>/', views.save_task, name='save_task'),
    path('change_task_status/', views.change_task_status, name='change_task_status'),    
    path('profile/', views.profile, name='profile'),
    path('subordinate_profile/<str:email>/', views.director_erp, name='subordinate_profile'),
]