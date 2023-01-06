from django import forms
from .models import Client, Service, Category


class Clientform(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'phone', 'profession']


class Serviceform(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'prix', 'category']
