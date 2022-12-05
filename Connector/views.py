from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Profile, Reservation


class ProfileList(generic.ListView):
    model = Profile
    queryset = Profile.objects.filter(status=0) | Profile.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 50


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
