
import django_filters
from django import forms
from .models import Match, Team, Tournament

class MatchFilter(django_filters.FilterSet):
    teams = django_filters.ModelChoiceFilter(
        queryset=Team.objects.all(),
        label='Team',
        method='filter_teams',
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
        fields = ['teams', 'tournament']

    def filter_teams(self, queryset, name, value):
        return queryset.filter(team1=value) | queryset.filter(team2=value)



# import django_filters
# from django import forms
# from django.db.models import Q
# from .models import Match, Team, Tournament, Innings


# class MatchFilter(django_filters.FilterSet):
#     teams = django_filters.ModelChoiceFilter(
#         queryset=Team.objects.all(),
#         label="Teams",
#         widget=forms.Select(
#             attrs={
#                 "class": "rounded-pill",
#                 "onchange": "this.form.submit()",
#                 "empty_label": "Teams",
#             }
#         ),
#     )
#     tournament = django_filters.ModelChoiceFilter(
#         queryset=Tournament.objects.all(),
#         label="Tournament",
#         widget=forms.Select(
#             attrs={
#                 "class": "rounded-pill",
#                 "onchange": "this.form.submit()",
#                 "empty_label": "Tournament",
#             }
#         ),
#     )

#     class Meta:
#         model = Match
#         fields = ["teams", "tournament"]



