from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Team, Match, Innings


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(5):
            match = Match.objects.get(pk=randint(Match.objects.first().pk, Match.objects.count()))
            batting_team = Team.objects.get(pk=randint(Team.objects.first().pk, Team.objects.count()))
            bowling_team = Team.objects.get(pk=randint(Team.objects.first().pk, Team.objects.count()))
            Innings.objects.get_or_create(
                batting_team=batting_team,
                bowling_team=bowling_team,
                match=match
            )
            self.stdout.write(self.style.SUCCESS(f"{batting_team} VS {bowling_team}"))
