from django.shortcuts import render
from science.models import Project as ScienceProject


# Create your views here.

def sciencehome(request):
    sci_projects = ScienceProject.objects.all().order_by('-date_started')
    return render(request, template_name='science/sciencehome.html', context={"sci_proj": sci_projects})
