from django.contrib import admin

# Register your models here.
from .models import Project, Event, Media
# Register your models here.

admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Media)
