from django import forms
from django.forms import DateInput

from .models import Match


class MatchCreateForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"
        exclude = ["winner"]
        widgets = {"match_date": DateInput(attrs={"type": "date"})}
