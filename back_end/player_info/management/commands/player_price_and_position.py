from django.core.management.base import BaseCommand

from web_scraping.player_price_and_position import get_fpl_data


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        get_fpl_data()
