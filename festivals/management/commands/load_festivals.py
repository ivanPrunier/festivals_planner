from django.core.management.base import BaseCommand

from festivals.models import Festival
from festivals.services.scraping import InfoconcertScraper


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        festivals = [
            'https://www.infoconcert.com/festival/we-love-green-7591/concerts.html',
            'https://www.infoconcert.com/festival/marvellous-island-8424/concerts.html',
            'https://www.infoconcert.com/festival/solidays-1696/concerts.html',
            'https://www.infoconcert.com/festival/garorock-1594/concerts.html',
            'https://www.infoconcert.com/festival/les-nuits-secretes-2480/concerts.html',
            'https://www.infoconcert.com/festival/rock-en-seine-2385/concerts.html',
            'https://www.infoconcert.com/festival/hellfest-2392/concerts.html'
        ]

        for festival_url in festivals:
            self.stdout.write(self.style.SUCCESS(f'Scraping {festival_url}.'))
            festival = Festival.objects.create(infoconcert_url=festival_url)
            InfoconcertScraper(festival).scrap()
            self.stdout.write(self.style.SUCCESS(f'Created festival {festival}.'))
