from django.db import models
import os

def icon_media_dir(instance,filename):
    # return the whole path to the file
    return os.path.join('icons', filename)

class ExternalWebsites(models.Model):
    external_link = models.URLField()
    icon = models.ImageField(upload_to=icon_media_dir, null=True)
    display_link = models.CharField(max_length=50, blank=True, null=True)

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    message = models.TextField(blank=True)
    date_sent = models.DateTimeField(auto_now_add=True, null=True)