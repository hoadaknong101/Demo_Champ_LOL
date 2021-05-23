from django import forms
from django.db.models import fields
from .models import Cosplay

class CosplayForm(forms.ModelForm):

    class Meta:
        model= Cosplay
        fields = '__all__'