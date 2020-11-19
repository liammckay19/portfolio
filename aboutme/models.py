from django.db import models
from datetime import datetime

from art.models import Project as ArtProjects
from science.models import Project as ScienceProjects

app_label = 'aboutme'


# Create your models here.
class Education(models.Model):
    school = models.CharField(verbose_name="School Name", max_length=100, default='')
    degree = models.CharField(verbose_name="Degree obtained", max_length=100, default='')
    date_graduated = models.DateField(verbose_name="Date Degree obtained", max_length=100)
    date_started = models.DateField(verbose_name="Date education started", max_length=100)
    description = models.CharField(verbose_name="Courses/skills used for degree", max_length=2000, default='')
    def __str__(self):
        return self.school

