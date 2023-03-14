from django.contrib import admin
from .models import CustomUser, location

admin.site.register(CustomUser)
admin.site.register(location)