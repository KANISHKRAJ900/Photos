from django.contrib import admin
from .models import daily

class dailyAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'img','sub_title')

# Register your models here.

admin.site.register(daily, dailyAdmin)