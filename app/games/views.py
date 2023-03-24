from django.shortcuts import render
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


# class BattingPerformanceCreateView(CreateView):
#     model = BattingPerformance


# class BattingPerformanceDetailView(DetailView):
#     model = BattingPerformance


# class BattingPerformanceListView(ListView):
#     model = BattingPerformance
