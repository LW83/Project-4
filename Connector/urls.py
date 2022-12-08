from . import views
from django.urls import path

urlpatterns = [
    path('', views.homeview, name='homepage'),
    path('profiles/', views.ProfileList.as_view(), name='profiles')
    # path('create_profile/', view.CreateProfile.as_view(), name='create_profile')
]