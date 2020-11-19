from django.contrib import admin
from django.urls import path
from . import views
app_name="art"
urlpatterns = [
    path('', views.arthome, name='home'),
]
