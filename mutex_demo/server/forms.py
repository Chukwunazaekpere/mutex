from django import forms
from .models import Logs

class LogForms(forms.ModelForm):
    class Meta:
        model = Logs
        fields = ["operation"]
    