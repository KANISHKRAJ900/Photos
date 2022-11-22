from django.contrib import admin
from .models import photo

class photoAdmin(admin.ModelAdmin):
    list_display = ['img']

# Register your models here.

admin.site.register(photo, photoAdmin)