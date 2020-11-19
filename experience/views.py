from django.shortcuts import render
from .models import Position
from art.models import Project as ArtProject


# Create your views here.
def experiencehome(request):
    job_experiences = Position.objects.all().order_by("-date_ended")
    art_projects = ArtProject.objects.all()
    return render(request, 'experience/experiencehome.html',
                  {'jobs': job_experiences, "art_proj": art_projects, })
