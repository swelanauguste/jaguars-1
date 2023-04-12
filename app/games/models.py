import math
from decimal import Decimal

from django.db import models
from django.urls import reverse

CHOICES = [(i, i) for i in range(12)]


class TimeStamp(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Team(TimeStamp):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("team-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Venue(TimeStamp):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Dismissal(TimeStamp):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name.lower()


class MatchTime(models.Model):
    time = models.TimeField()

    def __str__(self):
        return f"{self.time}"


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=4)

    class Meta:
        unique_together = ["name", "year"]

    def __str__(self):
        return f"{self.name} {self.year}"


class Match(TimeStamp):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, null=True, blank=True
    )
    match_date = models.DateField()
    match_time = models.ForeignKey(
        MatchTime, on_delete=models.CASCADE, null=True, blank=True
    )
    team1 = models.ForeignKey(
        Team, related_name="team1_matches", on_delete=models.CASCADE
    )
    team2 = models.ForeignKey(
        Team, related_name="team2_matches", on_delete=models.CASCADE
    )

    winner = models.ForeignKey(
        Team,
        related_name="winning_matches",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    venue = models.ForeignKey(
        Venue,
        related_name="venues",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name_plural = "matches"
        ordering = ("match_date", "match_time")

    def get_absolute_url(self):
        return reverse("match-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} - {self.match_date} - {self.match_time} - {self.venue}"


class Player(TimeStamp):
    name = models.CharField(max_length=100, unique=True)
    teams = models.ManyToManyField(Team, related_name="players")
    
    def get_absolute_url(self):
        return reverse("player-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Innings(TimeStamp):
    match = models.ForeignKey(Match, related_name="innings", on_delete=models.CASCADE)
    batting_team = models.ForeignKey(
        Team, related_name="batting_innings", on_delete=models.CASCADE
    )
    bowling_team = models.ForeignKey(
        Team, related_name="bowling_innings", on_delete=models.CASCADE
    )
    byes = models.IntegerField(default=0)
    leg_byes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "innings"
        ordering = ("-created",)

    def __str__(self):
        return f"{self.batting_team.name} innings in {self.match}"

    @property
    def get_wides(self):
        return sum(wide.wides for wide in self.bowling_performances.all())

    @property
    def get_no_balls(self):
        return sum(no_ball.no_balls for no_ball in self.bowling_performances.all())

    @property
    def get_total_extras(self):
        return self.get_no_balls + self.get_wides + self.byes + self.leg_byes

    @property
    def get_batters_total_score(self):
        return sum(runs.runs for runs in self.batting_performances.all())

    @property
    def get_total_score(self):
        return self.get_batters_total_score + self.get_total_extras

    def get_wickets(self):
        count = 0
        for out in self.batting_performances.all():
            if out.out:
                count = count + 1
        return count


class BattingPerformance(TimeStamp):
    innings = models.ForeignKey(
        Innings, related_name="batting_performances", on_delete=models.CASCADE
    )
    batted_at = models.IntegerField(choices=CHOICES, default=1)
    player = models.ForeignKey(
        Player, related_name="batting_performances", on_delete=models.CASCADE
    )
    how_out = models.ForeignKey(
        Dismissal, on_delete=models.CASCADE, null=True, blank=True
    )
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    out = models.BooleanField(default=1)

    class Meta:
        ordering = ("batted_at",)

    @property
    def get_strike_rate(self):
        if self.runs >= 1 and self.balls_faced >= 1:
            strike_rate = self.runs / self.balls_faced * 100
            return f"{strike_rate:.1f}"
        return 0

    

    def __str__(self):
        return f"{self.player} scored {self.runs} runs in {self.innings}"


class BowlingPerformance(TimeStamp):
    innings = models.ForeignKey(
        Innings, related_name="bowling_performances", on_delete=models.CASCADE
    )
    bowled_at = models.IntegerField(choices=CHOICES, default=1)
    player = models.ForeignKey(
        Player, related_name="bowling_performances", on_delete=models.CASCADE
    )
    overs = models.DecimalField(max_digits=3, decimal_places=1, default=4)
    runs_conceded = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    no_balls = models.IntegerField(default=0)
    wides = models.IntegerField(default=0)
    dots = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)

    class Meta:
        ordering = ("bowled_at",)

    @property
    def get_bowling_econ(self):
        if self.runs_conceded > 0 and self.overs > 0:
            econ = self.runs_conceded / self.overs
            return f"{econ:.1f}"
        return 0

    def __str__(self):
        return f"{self.player} took {self.wickets} wickets in {self.innings}"
