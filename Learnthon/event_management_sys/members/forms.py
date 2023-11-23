from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Event,User

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'venue_address']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'sex', 'email', 'phone_number', 'password1', 'password2']