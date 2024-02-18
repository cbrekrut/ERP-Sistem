from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("erp/", views.erp, name='erp'),
    path("customers/", views.customers, name='customers'),    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),    
]