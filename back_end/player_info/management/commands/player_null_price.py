from django.core.management.base import BaseCommand

from player_info.models import Player
from web_scraping.player_price_and_position import get_fpl_data
from pprint import pprint


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def handle(self, *args, **options):
        qs = Player.objects.filter(price=None)
        #found = 0
        print(qs.count())
        """
        for obj in qs:
            print(f'{obj.first_name if obj.first_name else ' '} {obj.middle_name if obj.middle_name else ' '} {obj.last_name if obj.last_name else ' '} {obj.team}')
        print(qs.count())
        """
        """
        for key, data in dict.items():
            if data['first_name'] and data['last_name'] and data['middle_name']:
                qs_ = qs.filter(first_name__icontains=data['first_name'], last_name__icontains=data['last_name'], middle_name__icontains=data['middle_name'], team=data['team'])
                if qs_:
                    #print(f'{qs_}  {data['first_name']} {data['middle_name']} {data['last_name']}')
                    found += 1
                    a = qs_.first()
                    a.position = data['pos']
                    a.price = data['price']
                    a.save()
                    continue
            if data['first_name'] and data['last_name']:
                qs_ = qs.filter(first_name__icontains=data['first_name'], last_name__icontains=data['last_name'], team=data['team'])
                if qs_:
                    #print(f'{qs_}  {data['first_name']} {data['last_name']}')
                    found += 1
                    a = qs_.first()
                    a.position = data['pos']
                    a.price = data['price']
                    a.save()
                    continue
            if data['first_name']:
                qs_ = qs.filter(first_name__icontains=data['first_name'], team=data['team'])
                if qs_:
                    #print(f'{qs_}  {data['first_name']}')
                    found += 1
                    a = qs_.first()
                    a.position = data['pos']
                    a.price = data['price']
                    a.save()
                    continue
            if data['last_name']:
                qs_ = qs.filter(first_name__icontains=data['last_name'], team=data['team'])
                if qs_:
                    #print(f'{qs_} {data['last_name']}')
                    found += 1
                    a = qs_.first()
                    a.position = data['pos']
                    a.price = data['price']
                    a.save()
                    continue
        """
        #print(f'found:{found} all:{qs.count()}')