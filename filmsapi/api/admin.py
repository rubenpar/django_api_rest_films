from django.contrib import admin

# Register your models here.
from .models import People, Studio,Film

admin.site.register(People)
admin.site.register(Studio)
admin.site.register(Film)