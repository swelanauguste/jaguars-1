from django.core.management.base import BaseCommand

from ...models import Player, Team

JAGUARS_TEAM_LIST = [
    "Swelan Auguste",
    "Jonathan Paul",
    "Aaron Joseph",
    "Joachim Robinson",
    "Kervon Louis",
    "Kendrick Williams",
    "Richard Cherry",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for row in JAGUARS_TEAM_LIST:
            name = row
            team = Team.objects.get(name__icontains="jaguars")
            players = []
            player = Player.objects.get_or_create(
                name=name,
            )
            player_list = Player.objects.get(name__icontains=name)
            players.append(player_list)
            for player in players:
                player.teams.add(team)
                self.stdout.write(self.style.SUCCESS(f"{player}"))
