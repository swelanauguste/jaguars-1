from django.core.management.base import BaseCommand

from ...models import Team

TEAM_LIST = [
    "Mighty B",
    "BTC",
    "Forestierre",
    "La Guerre",
    "NIC",
    "Jaguars",
    "SAB",
    "Monchy",
    "Marc",
    "Belmonite",
    "Dennery",
    "All Start",
    "DC United",
    "Raising Sun",
    "C Vests",
    "M Blasters"
]

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Team.objects.all().delete()
        for _ in TEAM_LIST:
            name = _
            Team.objects.get_or_create(
                name=name,
            )
            self.stdout.write(self.style.SUCCESS(f"{name}"))
