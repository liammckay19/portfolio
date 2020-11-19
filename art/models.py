from django.db import models
from django.utils import timezone
from portfolio.settings import MEDIA_ROOT
import datetime

from aboutme import models as aboutme
from experience import models as experience

app_label = 'art'


class Event(models.Model):
    title = models.CharField(verbose_name="Event title", max_length=200)
    organization = models.CharField(verbose_name="Company/Organization name", max_length=200)
    date_started = models.DateField(verbose_name='First day of event')
    date_ended = models.DateField(verbose_name='Last day of event', null=True, default=date_started)
    description = models.CharField(verbose_name='Event description/my role', max_length=2000)
    external_link = models.URLField(verbose_name='External link to website with detailed info')

    def __str__(self):
        return self.title


class Media(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created on this website')
    date_modified = models.DateTimeField(auto_now_add=True, verbose_name='Date changed on this website')
    date_recorded = models.DateField(verbose_name="Day media was recorded")
    upload = models.ImageField(upload_to='art/', null=True, blank=True)

    def __str__(self):
        return self.upload.name

class Project(models.Model):
    school = models.ForeignKey('aboutme.Education', verbose_name="School where project was performed", null=True,
                               blank=True, on_delete=models.CASCADE)
    work = models.ForeignKey('experience.Position', verbose_name="Job where project was performed", null=True,
                             blank=True, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name="Project title", max_length=200)
    location = models.CharField(verbose_name="Location name", max_length=200, default='')
    date_started = models.DateField(verbose_name='First day of project')
    date_ended = models.DateField(verbose_name='Last day of project', null=True, default=date_started)
    description = models.CharField(verbose_name='Project description/my role', max_length=2000)
    external_link = models.URLField(verbose_name='External link to website with detailed info')
    embedHTML = models.CharField(verbose_name='iframe or HTML to embed within thumbnail', max_length=2000, blank=True,
                                 null=True)
    skills = models.ManyToManyField('experience.Skill')
    thumbnail = models.ForeignKey(Media, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
