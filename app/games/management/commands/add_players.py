from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Player, Team


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(240):
            name = fake.simple_profile()['name']
            team = Team.objects.get(pk=randint(1, Team.objects.count()))
            Player.objects.get_or_create(
                name=name,
                team=team
            )
            self.stdout.write(self.style.SUCCESS(f"{name}"))
