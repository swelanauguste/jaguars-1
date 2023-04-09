import django_filters
from django import forms

from .models import Match, Team, Tournament


class MatchFilter(django_filters.FilterSet):
    team1 = django_filters.ModelChoiceFilter(
        queryset=Team.objects.all(),
        label="Teams",
        widget=forms.Select(
            attrs={
                "class": "rounded-pill",
                "onchange": "this.form.submit()",
                "empty_label": "Teams",
            }
        ),
    )
    tournament = django_filters.ModelChoiceFilter(
        queryset=Tournament.objects.all(),
        label="Tournament",
        widget=forms.Select(
            attrs={
                "class": "rounded-pill",
                "onchange": "this.form.submit()",
                "empty_label": "Tournament",
            }
        ),
    )

    class Meta:
        model = Match
        fields = ["team1", "tournament"]
