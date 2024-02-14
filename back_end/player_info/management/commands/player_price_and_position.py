from django.core.management.base import BaseCommand

import traceback

from django.db import transaction
from player_info.models import Player
from web_scraping.player_price_and_position import get_fpl_data

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                data_dict = get_fpl_data()
                first_last_dict = data_dict['first_last_dict']
                last_dict = data_dict['last_dict']
                first_dict = data_dict['first_dict']
                players_first_last_dict = {f'{player.first_name}-{player.last_name}-{player.team.team_code}':player for player in Player.objects.all()}
                players_last_dict = {f'{player.last_name}-{player.team.team_code}':player for player in Player.objects.all()}
                players_first_dict = {f'{player.first_name}-{player.team.team_code}':player for player in Player.objects.all()}
                list_to_update = []
                found = 0
                for key, data in first_last_dict.items():
                    if not key in players_first_last_dict:
                        continue

                    found += 1
                    player = players_first_last_dict[key]
                    player.price = data['price']
                    player.position = data['pos']

                    list_to_update.append(player)

                for key, data in last_dict.items():
                    if not key in players_last_dict:

                        if key in players_first_dict:
                            found += 1

                            player = players_first_dict[key]
                            player.price = data['price']
                            player.position = data['pos']

                            list_to_update.append(player)

                            continue

                        continue

                    found += 1

                    player = players_last_dict[key]
                    player.price = data['price']
                    player.position = data['pos']

                    list_to_update.append(player)

                for key, data in first_dict.items():
                    if not key in players_first_dict:

                        continue

                    found += 1

                    player = players_first_dict[key]
                    player.price = data['price']
                    player.position = data['pos']

                    list_to_update.append(player)

                Player.objects.bulk_update(list_to_update, fields=['price', 'position'])

        except:
            traceback.print_exc()

        finally:
            print(f'Found: {found}    Total players: {len(players_first_last_dict)}')