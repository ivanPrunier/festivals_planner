import requests
import datetime

from bs4 import BeautifulSoup

from festivals.models import Festival, Artist, Show
from django.core.exceptions import ObjectDoesNotExist


def generate_url(path):
    return f'https://www.infoconcert.com{path}'


class InfoconcertScraper:

    days = []

    def __init__(self, festival: Festival):
        self.festival = festival

    def scrap(self):
        result = requests.get(self.festival.infoconcert_url)
        result.raise_for_status()
        festival_soup = BeautifulSoup(result.content, 'html.parser')

        self.festival.name = festival_soup.find('section', {'class': 'single-intro'})\
            .find('h1', {'itemprop': 'name'})\
            .get_text()\
            .title()

        description_url = festival_soup.find('section', {'class': 'single-intro'})\
            .find('div', {'class': 'currentMenu'})\
            .find('ul', {'class': 'nav-tabs'})\
            .find_all('li')[1]\
            .find('a')['href']

        self.scrap_description(generate_url(description_url))

        for day in festival_soup.find_all('div', {'class': 'date-line-festival'}):
            day_url = day.find('div', {'class': 'more-infos'}).find('a')['href']
            self.scrap_day(generate_url(day_url))

        self.festival.start_date = self.days[0]
        self.festival.end_date = self.days[-1]

        self.festival.save()

    def scrap_description(self, description_url):
        result = requests.get(description_url)
        result.raise_for_status()
        description_soup = BeautifulSoup(result.content, 'html.parser')
        self.festival.description = description_soup.find('section', {'class': 'single-main-content'})\
            .find_all('div', {'class': 'description'})[0]\
            .get_text()

    def scrap_day(self, day_url):
        result = requests.get(day_url)
        result.raise_for_status()
        day_soup = BeautifulSoup(result.content, 'html.parser')
        date = datetime.datetime.strptime(day_soup.find('div', {'class': 'sheet-concert-header'}).find('time')['datetime'], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
        self.days.append(date)

        for artist_div in day_soup.find('div', {'id': 'messages'}).find_all('div', {'class': 'panel-body__content'}):
            artist = self.scrap_artist(artist_div)

            show = Show.objects.create(
                festival=self.festival,
                artist=artist,
                start_datetime=date,
                end_datetime=date,
            )
            print(f'Created show "{show}".')

        return

    def scrap_artist(self, artist_div):
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
            print(f'Created artist "{artist}".')

        return artist
