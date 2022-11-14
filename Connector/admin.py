from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

# @admin.register(Profile)
# class ProfilesAdmin(admin.ModelAdmin):
    
#     prepopulated_fields = {'slug':('dog_breed',)}