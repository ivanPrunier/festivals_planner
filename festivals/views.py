from rest_framework import viewsets, permissions

from festivals.models import Artist, Festival, Show

from festivals.serializers import FestivalSerializer, ArtistSerializer, ShowSerializer


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class ShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class FestivalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    # permission_classes = (permissions.IsAuthenticated,)
