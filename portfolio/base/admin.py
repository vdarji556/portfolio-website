from django.contrib import admin
from base.models import *
# Register your models here.

admin.site.register(Contect)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "get_technologies")

    def get_technologies(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()])
    get_technologies.short_description = "Technologies Used"

admin.site.register(Technology)
