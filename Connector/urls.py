from . import views
from django.urls import path

urlpatterns = [
    path('', views.homeview, name='homepage'),
    
    path('profiles/', views.ProfileList.as_view(), name='profiles'),

    # path('pound/', include(([
    #     path('', .as_view(), name=''),
    #     path('profile/add/', .as_view(), name='profile_add'),
    #     path('profile/<int:pk>/', .as_view(), name='profile_change'),
    #     path('profile/<int:pk>/delete/', .as_view(), name='profile_delete'),
    # ])))
       
    # path('create_profile/', view.CreateProfile.as_view(), name='create_profile')
]