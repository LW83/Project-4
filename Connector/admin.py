from django.contrib import admin
from .models import Profile, Reservations

# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pound', 'dog_breed', 'profile_added', 'status', 'urgency')
    search_fields = ['pound', 'dog_breed', 'urgency']
    list_filter = ('status', 'profile_added', 'urgency')


@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('status', 'rescue', 'comment', 'last_updated')
    list_filter = ('status', 'rescue')
    search_fields = ('status', 'rescue')
    # actions = ['approve_comments']
