from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView

from .models import BattingPerformance, Innings, Match, Team, Venue


class TealListView(ListView):
    model = Team


class TealDetailView(DetailView):
    model = Team


# class InningsDetailView(DetailView):
#     model = Innings


# class InningsListView(ListView):
#     model = Innings


class MatchDetailView(DetailView):
    model = Match


class MatchListView(ListView):
    model = Match
    teams = Team.objects.all()

    extra_context = {"teams": teams}

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Match.objects.filter(
                Q(team1__name__icontains=query) | Q(team2__name__icontains=query)
            ).distinct()
        else:
            return Match.objects.all()


# class BattingPerformanceCreateView(CreateView):
#     model = BattingPerformance


# class BattingPerformanceDetailView(DetailView):
#     model = BattingPerformance


# class BattingPerformanceListView(ListView):
#     model = BattingPerformance
