from django.core.management.base import BaseCommand

from ...models import Group

CATEGORY_LIST = [
    "computer",
    "printer",
    "scanner",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in CATEGORY_LIST:
            name = _.lower()
            Group.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS(f"{name}"))