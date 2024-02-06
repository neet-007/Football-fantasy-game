from django.core.management.base import BaseCommand

from web_scraping.player_injuries import get_injuries_and_suspensions


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        get_injuries_and_suspensions()
