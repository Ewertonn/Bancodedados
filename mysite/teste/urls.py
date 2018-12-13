from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.perfilformulario.as_view(), name='login')
    ]