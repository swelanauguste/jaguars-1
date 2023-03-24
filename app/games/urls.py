from django.urls import path

from .views import MatchDetailView, MatchListView  # BattingPerformanceCreateView,

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
    # path(
    #     "batting-create/", MatchCreateView.as_view(), name="batting-create"
    # ),
]
