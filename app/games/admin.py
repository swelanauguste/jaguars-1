from django.contrib import admin

from .models import (
    BattingPerformance,
    BowlingPerformance,
    Dismissal,
    Innings,
    Match,
    Player,
    Team,
    Venue,
    MatchTime
)

admin.site.register(Team)
admin.site.register(Venue)
admin.site.register(Dismissal)
admin.site.register(MatchTime)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "team")


admin.site.register(Player, PlayerAdmin)


# admin.site.register(BattingPerformance)
# admin.site.register(BowlingPerformance)
# admin.site.register(Match)

# admin.site.register(Innings)


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
