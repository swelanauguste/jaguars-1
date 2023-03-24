from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Team, Venue, Match


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(5):
            team1 = Team.objects.get(pk=randint(Team.objects.first().pk, Team.objects.count()))
            team2 = Team.objects.get(pk=randint(Team.objects.first().pk, Team.objects.count()))
            match_date=fake.date_this_month()
            venue = Venue.objects.get(pk=randint(Venue.objects.first().pk, Venue.objects.count()))
            winner = Team.objects.get(pk=randint(Team.objects.first().pk, Team.objects.count()))
            Match.objects.get_or_create(
                team1=team1,
                team2=team2,
                match_date=match_date,
                venue=venue,
                winner=winner,
            )
            self.stdout.write(self.style.SUCCESS(f"{team1} VS {team2}"))
