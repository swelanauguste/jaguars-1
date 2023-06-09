from django.contrib import admin

from .models import (
    BattingPerformance,
    BowlingPerformance,
    Dismissal,
    Innings,
    Match,
    MatchTime,
    Player,
    Team,
    Tournament,
    Venue,
)

admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Venue)
admin.site.register(Dismissal)
admin.site.register(MatchTime)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Player, PlayerAdmin)


# admin.site.register(BattingPerformance)
# admin.site.register(BowlingPerformance)
# admin.site.register(Match)

# admin.site.register(Innings)


@admin.register(BattingPerformance)
class BattingPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "batted_at",
        "player",
        "how_out",
        "runs",
        "balls_faced",
        "fours",
        "sixes",
        "out",
        "get_strike_rate",
    )


@admin.register(BowlingPerformance)
class BowlingPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "bowled_at",
        "player",
        "overs",
        "runs_conceded",
        "wickets",
        "no_balls",
        "wides",
        "dots",
        "fours",
        "sixes",
        "get_bowling_econ",
    )
class BattingInLine(admin.TabularInline):
    model = BattingPerformance
    extra = 11


class BowlingInLine(admin.TabularInline):
    model = BowlingPerformance
    extra = 11


class InningsAdmin(admin.ModelAdmin):
    list_display = (
        "match",
        "batting_team",
        "bowling_team",
        "get_total_score",
        "get_wickets",
    )
    inlines = [BattingInLine, BowlingInLine]


admin.site.register(Innings, InningsAdmin)
#


class InningsInLine(admin.TabularInline):
    model = Innings
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    inlines = [InningsInLine]


admin.site.register(Match, MatchAdmin)
