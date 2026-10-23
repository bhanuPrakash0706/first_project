        
from django import forms
from .models import resverations


class ReservationsFrom(forms.ModelForm):
    class Meta:
        model = resverations
        fields = '__all__'