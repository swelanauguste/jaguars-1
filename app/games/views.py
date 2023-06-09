from datetime import datetime, timedelta

from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .filters import MatchFilter
from .forms import MatchCreateForm
from .models import (
    BattingPerformance,
    BowlingPerformance,
    Innings,
    Match,
    Player,
    Team,
    Tournament,
    Venue,
)


class PlayerListView(ListView):
    model = Player


class PlayerDetailView(DetailView):
    model = Player


class PlayerUpdateView(UpdateView):
    model = Player
    fields = "__all__"


class PlayerCreateView(CreateView):
    model = Player
    fields = "__all__"


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
    today = datetime.now().date()
    week_ago = today + timedelta(-7)
    queryset = Match.objects.filter(match_date__gte=week_ago)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MatchFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


# class BattingPerformanceCreateView(CreateView):
#     model = BattingPerformance


# class BattingPerformanceDetailView(DetailView):
#     model = BattingPerformance


# class BattingPerformanceListView(ListView):
#     model = BattingPerformance
