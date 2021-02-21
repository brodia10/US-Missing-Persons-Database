from django.core.management.base import BaseCommand, CommandError
from usmp.core.models.world_boarder import load


class Command(BaseCommand):
    help = "Imports initial world boarders data into dB"

    def handle(self, *args, **options):
        load()
        self.stdout.write(self.style.SUCCESS("Successfully ingested all world boarders data"))
