from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Profile


class ProfileList(generic.ListView):
    model = Profile
    queryset = Profile.objects.filter(status=0) | Profile.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 50


