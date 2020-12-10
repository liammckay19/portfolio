import random

from django.db import models
from django.utils import timezone
import os

app_label = "experience"


class Skill(models.Model):
    COLORS = (
        ("#ff4845", "red"),
        ("#4e93ff", "blue"),
        ("#686668", "grey"),
        ("#24a944", "green"),
        ("#ffa051", "orange"),
    )
    skill = models.CharField(verbose_name="Skill name", max_length=50)
    color = models.CharField(choices=COLORS, max_length=40, default="#000")

    def __str__(self):
        return self.skill


# Create your models here.
class Position(models.Model):
    ordering = ['-date_started']

    title = models.CharField(verbose_name='Job title', max_length=200)
    organization = models.CharField(verbose_name="Company/Organization name", max_length=200, default='')
    date_started = models.DateField(verbose_name='First day of work')
    date_ended = models.DateField(verbose_name='Last day of work', null=True, default=timezone.now)
    description = models.CharField(verbose_name='Duties performed', max_length=2000)
    external_link = models.URLField(verbose_name='External link to website with detailed info')
    address = models.CharField(verbose_name="Company/Organization address", max_length=200, default='')
    country = models.CharField(verbose_name="Company/Organization country", max_length=200, default='')
    supervisor_name = models.CharField(verbose_name="Company/Organization supervisor full name", max_length=200,
                                       default='')
    supervisor_title = models.CharField(verbose_name="Company/Organization supervisor job title", max_length=200,
                                        default='')
    supervisor_email = models.CharField(verbose_name="Company/Organization supervisor email", max_length=200,
                                        default='')
    thumbnail_filename = models.CharField(verbose_name="File name for image", max_length=100, default='')

    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title
