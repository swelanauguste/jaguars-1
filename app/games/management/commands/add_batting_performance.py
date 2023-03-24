from random import randint

from django.core.management.base import BaseCommand

from ...models import BattingPerformance, Dismissal, Innings, Match, Player


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in range(5):
            innings = Innings.objects.get(pk=Innings.objects.first().pk)
            for _ in range(6):
                player = Player.objects.get(
                    pk=randint(Player.objects.first().pk, Player.objects.count())
                )
                runs = randint(0, 44)
                balls_faced = randint(0, 34)
                fours = randint(0, 5)
                sixes = randint(0, 2)
                out = randint(0, 1)
                how_out = Dismissal.objects.get(
                    pk=randint(Player.objects.first().pk, Dismissal.objects.count())
                )
            BattingPerformance.objects.get_or_create(
                innings=innings,
                player=player,
                runs=runs,
                balls_faced=balls_faced,
                fours=fours,
                sixes=sixes,
                out=out,
                how_out=how_out,
            )
            self.stdout.write(self.style.SUCCESS(f"{player}"))
