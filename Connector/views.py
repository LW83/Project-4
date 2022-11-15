from django.shortcuts import render
from django.views import generic
from .models import Profile


class ProfileList(generic.ListView):
    model = Profile
    queryset = Profile.objects.filter(status=0).order_by('-urgency', 'profile_added')
    template_name = 'index.html'
    paginate_by = 50
