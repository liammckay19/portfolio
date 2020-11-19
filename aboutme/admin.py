from django.contrib import admin
from .models import Education


# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display = ("date_graduated",
                    "date_started",
                    "degree",
                    "description",
                    "school")


admin.site.register(Education, EducationAdmin)
