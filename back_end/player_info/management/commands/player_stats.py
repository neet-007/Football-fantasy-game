from django.core.management.base import BaseCommand

from web_scraping.player_stats import GetPlayerStats


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        GetPlayerStats().get_player_stats()
