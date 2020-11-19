from django.shortcuts import render
from .models import Education
# Create your views here.

# Create your views here.
def aboutmehome(request):
    education = Education.objects.all()
    return render(request, template_name='aboutme/aboutmehome.html', context={'education':education})