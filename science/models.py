from django.db import models
from experience import models as experience

from portfolio.settings import MEDIA_ROOT
import os


def sci_media_dir(instance,filename):
    # return the whole path to the file
    return os.path.join('science', filename)

class Media(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created on this website')
    date_modified = models.DateTimeField(verbose_name='Date changed on this website',
                                         auto_now_add=True)
    date_recorded = models.DateField(verbose_name="Day media was recorded")
    upload = models.ImageField(upload_to=sci_media_dir)
    def __str__(self):
        return self.upload.name


class Event(models.Model):
    title = models.CharField(verbose_name="Event title", max_length=200)
    organization = models.CharField(verbose_name="Company/Organization name", max_length=200)
    date_started = models.DateField(verbose_name='First day of event')
    date_ended = models.DateField(verbose_name='Last day of event', null=True, default=date_started)
    description = models.CharField(verbose_name='Event description/my role', max_length=2000)
    external_link = models.URLField(verbose_name='External link to website with detailed info')

    def __str__(self):
        return self.title


class Project(models.Model):
    ordering = ['-date_ended']

    title = models.CharField(verbose_name="Project title", max_length=200)
    organization = models.CharField(verbose_name="Company/Organization name", max_length=200)
    date_started = models.DateField(verbose_name='First day of project')
    date_ended = models.DateField(verbose_name='Last day of project', null=True, default=date_started)
    description = models.CharField(verbose_name='Project description/my role', max_length=2000)
    external_link = models.URLField(verbose_name='External link to website with detailed info', blank=True)
    skills = models.ManyToManyField('experience.Skill', related_name='scienceSkill')
    thumbnail = models.ForeignKey(Media, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
