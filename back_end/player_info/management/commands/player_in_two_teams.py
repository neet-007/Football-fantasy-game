from django.core.management.base import BaseCommand

import traceback

from django.db import transaction
from player_info.models import Player
from web_scraping.player_price_and_position import get_fpl_data_one_dict
from django.db.models.query import QuerySet


def compare(queryset:QuerySet) -> set:
    querylist = list(queryset)
    return_set = set()
    for i in range(len(queryset)):
        for j in range(i + 1, len(queryset)):
            if querylist[i].nation == querylist[j].nation and querylist[i].age == querylist[j].age:
                return_set.add(f'{querylist[i].first_name} {querylist[i].last_name} {querylist[i].team.team_code} {querylist[i].price}')
                return_set.add(f'{querylist[j].first_name} {querylist[j].last_name} {querylist[j].team.team_code} {querylist[j].price}')
                if querylist[i].price and not querylist[j].price:
                    querylist[j].delete()

                elif not querylist[i].price and querylist[j].price:
                    querylist[i].delete()

    if return_set:
        print(queryset)
        print(return_set)

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                dict = get_fpl_data_one_dict()
                for keys, data in dict.items():
                    if data['first_name'] and data['last_name']:
                        qs = Player.objects.filter(first_name=data['first_name'], last_name=data['last_name'])
                        if qs.count() > 1:
                            compare(qs)
                    if data['first_name']:
                        qs = Player.objects.filter(first_name=data['first_name'])
                        if qs.count() > 1:
                            compare(qs)
                    if data['last_name']:
                        qs = Player.objects.filter(last_name=data['last_name'])
                        if qs.count() > 1:
                            compare(qs)

        except:
            traceback.print_exc()

        finally:
            print(f'players with no price:{Player.objects.filter(price=None).count()}.')