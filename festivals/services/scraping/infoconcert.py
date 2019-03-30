import requests
import datetime

from bs4 import BeautifulSoup

from festivals.models import Festival, Artist, Show
from django.core.exceptions import ObjectDoesNotExist


def generate_url(path):
    return f'https://www.infoconcert.com{path}'


class InfoconcertScraper:

    def __init__(self, festival: Festival):
        self.festival = festival

    def scrap(self):
        result = requests.get(self.festival.infoconcert_url)
        result.raise_for_status()
        soup = BeautifulSoup(result.content, 'html.parser')

        for day in soup.find_all('div', {'class': 'date-line-festival'}):
            day_url = day.find('div', {'class': 'more-infos'}).find('a')['href']
            self.scrap_day(generate_url(day_url))

    def scrap_day(self, day_url):
        result = requests.get(day_url)
        result.raise_for_status()
        soup = BeautifulSoup(result.content, 'html.parser')

        for artist_div in soup.find('div', {'id': 'messages'}).find_all('div', {'class': 'panel-body__content'}):
            artist_title = artist_div.find("h4").find("a")
            artist_url = generate_url(artist_title['href'])
            try:
                artist = Artist.objects.get(infoconcert_url=artist_url)
            except (ObjectDoesNotExist, Artist.DoesNotExist):
                description = artist_div.find('p', {'class': 'description'}).get_text()
                artist = Artist.objects.create(
                    name=artist_title.get_text().title(),
                    description=description,
                    infoconcert_url=artist_url,
                )
            show = Show.objects.create(
                festival=self.festival,
                artist=artist,
                start_datetime=self.festival.start_date,
                end_datetime=self.festival.end_date,
            )
            print(f'Created show "{show}".')