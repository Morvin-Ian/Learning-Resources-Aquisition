from django import forms
from django.contrib.auth.models import User
from .models import Borrowed_Resource


class ResourceForm(forms.ModelForm):
    class Meta():
        model= Borrowed_Resource
        fields = ['borrowed','recorded_returning_date']
