from django.urls import path

from .views import (
    MatchCreateView,
    MatchDetailView,
    MatchListView,
    MatchUpdateView,
    TeamCreateView,
    TeamDetailView,
    TeamListView,
    TeamUpdateView,
)

urlpatterns = [
    path("", MatchListView.as_view(), name="match-list"),
    path("match/add/", MatchCreateView.as_view(), name="match-create"),
    path(
        "match/edit/<int:pk>/",
        MatchUpdateView.as_view(),
        name="match-update",
    ),
    path(
        "match/detail/<int:pk>/",
        MatchDetailView.as_view(),
        name="match-detail",
    ),
    path("teams", TeamListView.as_view(), name="teams"),
    path("teams/add/", TeamCreateView.as_view(), name="team-create"),
    path("team/detail/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("team/edit/<int:pk>/", TeamUpdateView.as_view(), name="team-update"),
]
