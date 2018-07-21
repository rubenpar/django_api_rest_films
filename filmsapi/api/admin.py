from django.contrib import admin

# Register your models here.
from .models import People, Studio

admin.site.register(People)
admin.site.register(Studio)