from django.core.management.base import BaseCommand

from ...models import Dismissal

DISMISSAL_LIST = [
    "BOWLED",
    "CAUGHT",
    "RUN-OUT",
    "STUMPED",
    "NOT-OUT",
]

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Dismissal.objects.all().delete()
        for _ in DISMISSAL_LIST:
            name = _
            Dismissal.objects.get_or_create(
                name=name,
            )
            self.stdout.write(self.style.SUCCESS(f"{name}"))
