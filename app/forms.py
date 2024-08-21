from django import forms
from .models import Rdv


class RdvForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = ['date', 'time', 'entreprise', 'nombreVisiteur']
