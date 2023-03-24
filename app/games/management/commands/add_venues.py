from django.core.management.base import BaseCommand

from ...models import Venue

VENUE_LIST = [
    "Grand Rev",
    "Forestierre",
    "Mabouya",
    "Balata",
    "Belair",
    "Monchy",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Venue.objects.all().delete()
        for _ in VENUE_LIST:
            name = _
            Venue.objects.get_or_create(
                name=name,
            )
            self.stdout.write(self.style.SUCCESS(f"{name}"))
