from django.contrib import admin

# Register your models here.
from .models import Position, Skill


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organization',
        'external_link',
        'date_started',
        'date_ended',
        'supervisor_name',
        'supervisor_title',
        'supervisor_email',
    )


admin.site.register(Position, PositionAdmin)
admin.site.register(Skill)