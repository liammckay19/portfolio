from django.contrib import admin
from .models import Contact, ExternalWebsites


# Register your models here.
admin.site.register(Contact)
admin.site.register(ExternalWebsites)