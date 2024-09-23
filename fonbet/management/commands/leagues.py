from django.core.management.base import BaseCommand
import requests
from ...models import RemoteSport
from usage.models import Category
from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        res = requests.get('https://line53w.bk6bba-resources.com/events/listBase?lang=ru&scopeMarket=1600')
        for x in res.json()['sports']:
