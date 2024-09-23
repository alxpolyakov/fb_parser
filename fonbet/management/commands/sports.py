from django.core.management.base import BaseCommand
import requests
from ...models import RemoteSport
from usage.models import Category
from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        res = requests.get('https://line53w.bk6bba-resources.com/events/listBase?lang=ru&scopeMarket=1600')
        for x in res.json()['sports']:

            if x['kind'] != 'sport':
                continue
            print(x['name'])
            rs = RemoteSport.objects.get_or_create(
                remote_id=x['id'],
                defaults={
                    'name': x['name'], 'alias': x['alias'], 'sort_order': x['sortOrder']
                }
            )[0]
            if Category.objects.filter(name=rs.name).exists():
                rs.local_sport = Category.objects.get(name=rs.name)
                rs.save()
                continue
            c = Category.objects.get_or_create(name=rs.name, slug=rs.alias, defaults={
                'created_at': now(), 'updated_at': now(), 'status': 1
            })[0]
            rs.local_sport = c
            rs.save()

