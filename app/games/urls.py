from django.urls import path

from .views import MatchDetailView, MatchListView, TealListView, TealDetailView

# from .views import (
#     BattingPerformanceCreateView,
#     BattingPerformanceDetailView,
#     BattingPerformanceListView,
# )


urlpatterns = [
    path("", MatchListView.as_view(), name="list"),
    path(
        "detail/<int:pk>/",
        MatchDetailView.as_view(),
        name="detail",
    ),
    path("teams", TealListView.as_view(), name="teams"),
    path("team/detail/<int:pk>/", TealDetailView.as_view(), name="team-detail"),
]
