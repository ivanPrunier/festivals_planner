from rest_framework import serializers

from festivals.models import Artist, Festival, Show


class ShowSerializer(serializers.ModelSerializer):
    festival = serializers.SerializerMethodField()
    artist = serializers.SerializerMethodField()
    stage = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = ('id', 'name', 'artist', 'start_datetime', 'end_datetime', 'festival', 'stage')

    def get_festival(self, show):
        return {
            'id': show.festival.id,
            'name': show.festival.name,
            'description': show.festival.description,
            'start_date': show.festival.start_date,
            'end_date': show.festival.end_date,
        }

    def get_artist(self, show):
        return {
            'id': show.artist.id,
            'name': show.artist.name,
            'description': show.artist.description,
        }

    def get_stage(self, show):
        return {
            'id': show.stage.id,
            'name': show.stage.name,
            'description': show.stage.description,
        } if show.stage else None


class ArtistSerializer(serializers.ModelSerializer):
    tour = ShowSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'description', 'tour',)


class FestivalSerializer(serializers.ModelSerializer):
    line_up = ShowSerializer(many=True)

    class Meta:
        model = Festival
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'address', 'zip_code',
                  'city', 'line_up')

