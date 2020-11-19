from django.contrib import admin
from django.urls import path
from . import views
app_name = "contact"
urlpatterns = [
    path('', views.contacthome, name='home'),
    path('success', views.contactsuccess, name='success'),
]
