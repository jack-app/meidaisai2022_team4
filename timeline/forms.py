from attr import field
from django import forms
from .models import Event


class EventPostForm(forms.ModelForm):
    class Meta():
        model = Event
        fields = ('name', 'content')