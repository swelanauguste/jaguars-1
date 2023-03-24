from random import randint

from django.core.management.base import BaseCommand

from ...models import BowlingPerformance, Innings, Player


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in range(5):
            innings = Innings.objects.get(pk=Innings.objects.first().pk)
            player = Player.objects.get(
                pk=randint(Player.objects.first().pk, Player.objects.count())
            )
            overs = randint(1, 4)
            runs_conceded = randint(0, 30)
            wickets = randint(0, 3)
            BowlingPerformance.objects.get_or_create(
                innings=innings,
                player=player,
                overs=overs,
                runs_conceded=runs_conceded,
                wickets=wickets,
            )
            self.stdout.write(self.style.SUCCESS(f"{player}"))
