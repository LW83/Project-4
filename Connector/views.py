from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Reservation
from .forms import ProfileForm


class ProfileList(LoginRequiredMixin, generic.ListView):
    model = Profile
    queryset = Profile.objects.filter(status=0) | Profile.objects.filter(status=1)
    context_object_name = 'profiles'
    template_name = 'index.html'
    paginate_by = 50


def homeview(request):
    return render(request, 'home.html',)


# class CreateProfile(LoginRequiredMixin, generic.CreateView):
#     def get(self, request, *args, **kwargs):

#         return render(
#             request,
#             "create_profile.html",
#             {
#                 "profile_form": ProfileForm(),
#                 # "viewer_access": check_viewer_exists(request)
#             }
#         )


# class ProfileReservation(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Profile.objects.filter(status=0) | Profile.objects.filter(status=1)
#         profile = get_object_or_404(queryset, slug=slug)
#         reservations = Profile.reserve_pet.filter(approved=True)

#         return render(
#             request,
#             "index.html",
#             {
#                 "profile": profile,
#                 "reservation": reservations
#             },
#         )
