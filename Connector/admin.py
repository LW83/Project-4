from django.contrib import admin
from .models import Profiles

admin.site.register(Profiles)

# @admin.register(Profiles)
# class ProfilesAdmin(admin.ModelAdmin):
    
#     prepopulated_fields = {'slug':('dog_breed',)}