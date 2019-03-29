from rest_framework import viewsets

from festivals.models import Artist, Festival, Show

from festivals.serializers import FestivalSerializer, ArtistSerializer, ShowSerializer


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class FestivalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
