from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dog_breed', 'gender', 'approx_age', 'neutered', 'microchipped', 'circumstance', 'pound_entry_date', 'hold_date', 'status', 'urgency')
