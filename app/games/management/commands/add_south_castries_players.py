from django.core.management.base import BaseCommand

from ...models import Player, Team

SOUTH_CASTRIES_TEAM_LIST = [
    "Johnson Charles",
    "Kensely Paul",
    "Kemrol Charles",
    "Noelle Leo",
    "Aaron Joseph",
    "Wade Clovis",
    "Shervon Leo",
    "Tonius Simon",
    "Wendell Inglis",
    "Avalinus Callendar",
    "Lerry Auguste",
    "Kenrick James",
    "Malcolm  Monrose",
    "Gilbere Daniel",
    "Emerson Charles",
    "Swelan Auguste",
    "Anderson Charles",
    "Mugaran Shoulette",
    "Xavier Gabriel",
    "Daniel Jn Baptiste",
    "Kester Charlemagne",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for row in SOUTH_CASTRIES_TEAM_LIST:
            name = row
            team = Team.objects.get(name__icontains="south castries")
            players = []
            player = Player.objects.get_or_create(
                name=name,
            )
            player_list = Player.objects.get(name__icontains=name)
            players.append(player_list)
            for player in players:
                player.teams.add(team)
                self.stdout.write(self.style.SUCCESS(f"{player}"))
