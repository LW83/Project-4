from .models import Profile, User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class PoundSignUpForm(UserCreationForm):
    '''
    From Simpleisbetterthancomplex.com blog
    '''
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pound = True
        if commit:
            user.save()
        return user


class RescueSignUpForm(UserCreationForm):
    '''
    From Simpleisbetterthancomplex.com blog
    '''
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_rescue = True
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dog_breed', 'gender', 'approx_age', 'neutered', 'microchipped', 'circumstance', 'pound_entry_date', 'hold_date', 'status', 'urgency')
