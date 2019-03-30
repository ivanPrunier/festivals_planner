from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from festivals.models import Festival
from festivals.services.scraping import InfoconcertScraper


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Festival)
def scrap_festival_data(sender, instance=None, created=False, **kwargs):
    if created:
        InfoconcertScraper(instance).scrap()