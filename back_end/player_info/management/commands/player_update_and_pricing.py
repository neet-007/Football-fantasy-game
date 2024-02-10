from django.core.management.base import BaseCommand

from web_scraping.player_update_pricing import PlayerPricing


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        a = PlayerPricing()
        a.player_update_and_pricing()
