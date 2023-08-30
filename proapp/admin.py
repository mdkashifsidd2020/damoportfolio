from django.contrib import admin
from .models import dform
# Register your models here.

class adminclass(admin.ModelAdmin):
    list_display=['name','email','subject','message']

admin.site.register(dform,adminclass)