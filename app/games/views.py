from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView
from datetime import datetime
from .models import BattingPerformance, Innings, Match, Team, Tournament, Venue


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
