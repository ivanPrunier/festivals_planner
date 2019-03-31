from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Festival, Artist


@register(Artist)
class ArtistIndex(AlgoliaIndex):
    settings = {'searchableAttributes': ['name']}
    index_name = 'artists'


@register(Festival)
class FestivalIndex(AlgoliaIndex):
    settings = {'searchableAttributes': ['name']}
    index_name = 'festivals'