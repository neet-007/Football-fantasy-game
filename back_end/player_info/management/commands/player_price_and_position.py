from django.core.management.base import BaseCommand

from player_info.models import Player
from web_scraping.player_price_and_position import get_fpl_data

import unicodedata
import re

def normalize_name(name):
    # Normalize to NFKD Unicode form to separate diacritics
    normalized_name = unicodedata.normalize('NFKD', name)
    # Remove any character that is not a letter, digit, or whitespace
    normalized_name = re.sub(r'[^\w\s]', '', normalized_name)
    # Convert to lowercase
    normalized_name = normalized_name.lower()
    # Remove leading and trailing whitespaces
    normalized_name = normalized_name.strip()
    return normalized_name

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        data_dict = get_fpl_data()
        print(data_dict)
        found = 0

        for key, data in data_dict.items():
            if data['first_name'] and data['last_name'] and data['middle_name']:

                qs = Player.objects.filter(
                    first_name=data['first_name'],
                    middle_name=data['middle_name'],
                    last_name=data['last_name'],
                    team=data['team']
                )

                if qs.exists():
                    if qs.count() > 1:
                        print(f'Found more than one player {data['last_name']} {data['team']}')
                        continue

                    player = qs.first()
                    player.position = data['pos']
                    player.price = data['price']
                    player.save()
                    found += 1
                    continue

            if data['first_name'] and data['last_name']:
                if data['first_name'] == 'diogo':
                    print(1)
                qs = Player.objects.filter(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    team=data['team']
                )

                if qs.exists():
                    if qs.count() > 1:
                        print(f'Found more than one player {data['last_name']}')
                        continue

                    player = qs.first()
                    player.position = data['pos']
                    player.price = data['price']
                    player.save()
                    found += 1
                    continue

            if data['first_name']:
                if data['first_name'] == 'diogo':
                    print(2)
                qs = Player.objects.filter(
                    first_name=data['first_name'],
                    team=data['team']
                )

                if qs.exists():
                    if qs.count() > 1:
                        print(f'Found more than one player {data['last_name']}')
                        continue

                    player = qs.first()
                    player.position = data['pos']
                    player.price = data['price']
                    player.save()
                    found += 1
                    continue

            if data['last_name']:
                if data['first_name'] == 'diogo':
                    print(3)
                qs = Player.objects.filter(
                    last_name=data['last_name'],
                    team=data['team']
                )
                if qs.exists():
                    if qs.count() > 1:
                        print(f'Found more than one player {data['last_name']}')
                        continue

                    player = qs.first()
                    player.position = data['pos']
                    player.price = data['price']
                    player.save()
                    found += 1
                    continue

        print(f'Found: {found}    Total players: {Player.objects.all().count()}')

