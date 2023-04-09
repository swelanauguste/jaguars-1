from datetime import datetime

from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import BattingPerformance, Innings, Match, Team, Tournament, Venue
from .forms import MatchCreateForm

class TeamListView(ListView):
    model = Team


class TeamDetailView(DetailView):
    model = Team


class TeamUpdateView(UpdateView):
    model = Team
    fields = "__all__"


class TeamCreateView(CreateView):
    model = Team
    fields = "__all__"


class MatchDetailView(DetailView):
    model = Match


class MatchCreateView(CreateView):
    model = Match
    form_class = MatchCreateForm


class MatchUpdateView(UpdateView):
    model = Match
    fields = "__all__"


class MatchListView(ListView):
    model = Match
    teams = Team.objects.all()
    tournaments = Tournament.objects.all()

    extra_context = {"teams": teams, "tournaments": tournaments}

    def get_queryset(self):
        query1 = self.request.GET.get("team")
        query2 = self.request.GET.get("tournament")
        if query1 or query2:
            query = query1 + query2
            return Match.objects.filter(
                Q(team1__name__icontains=query)
                | Q(team2__name__icontains=query)
                | Q(tournament__name__icontains=query)
            ).distinct()
        else:
            return Match.objects.filter(match_date__gte=datetime.today())


# class BattingPerformanceCreateView(CreateView):
#     model = BattingPerformance


# class BattingPerformanceDetailView(DetailView):
#     model = BattingPerformance


# class BattingPerformanceListView(ListView):
#     model = BattingPerformance
