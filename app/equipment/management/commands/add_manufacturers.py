from django.core.management.base import BaseCommand

from ...models import Manufacturer

MANUFACTURER_LIST = [
    "HP",
    "DELL",
    "LENOVO",
    "XEROX",
    "HP",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in MANUFACTURER_LIST:
            name = _.lower()
            Manufacturer.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS(f"{name}"))