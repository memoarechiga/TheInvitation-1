from django.contrib import admin
from .models import Profile
from coolapp.models import UserGallery


admin.site.register(Profile)
admin.site.register(UserGallery)