from django.shortcuts import render
from art.models import Project as ArtProject

# Create your views here.
def arthome(request):
    art_projects = ArtProject.objects.all().order_by('-date_started')
    return render(request, template_name='art/arthome.html', context={"art_proj": art_projects})
