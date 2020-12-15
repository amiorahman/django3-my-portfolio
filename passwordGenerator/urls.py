from django.urls import path, include
from . import views

app_name = 'passwordGenerator'

urlpatterns = [
    path('', views.password_generator_home, name='password_generator_home'),
    path('password/', views.password_generated, name='password_generated'),
]