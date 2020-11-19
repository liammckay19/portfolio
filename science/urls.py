from django.contrib import admin
from django.urls import path
from . import views

app_name='science'
urlpatterns = [
    path('', views.sciencehome, name='home'),
]
