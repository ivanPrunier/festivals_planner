from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from festivals.models import Artist, Festival, Show, Participation, Attendance, Party, Task, \
    PartyInvite


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


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


class ParticipationSerializer(serializers.ModelSerializer):
    festival = serializers.SerializerMethodField()
    festival_id = serializers.PrimaryKeyRelatedField(
        source='festival',
        queryset=Festival.objects.all()
    )
    user = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Participation
        fields = ('id', 'festival', 'festival_id', 'user', 'start_date', 'end_date',)

    def get_festival(self, participation):
        return {
            'id': participation.festival.id,
            'name': participation.festival.name,
            'description': participation.festival.description,
            'start_date': participation.festival.start_date,
            'end_date': participation.festival.end_date,
        }


class AttendanceSerializer(serializers.ModelSerializer):
    participation = ParticipationSerializer(required=False)
    participation_id = serializers.PrimaryKeyRelatedField(
        source='participation',
        queryset=Participation.objects.all(),
    )
    show = ShowSerializer(required=False)
    show_id = serializers.PrimaryKeyRelatedField(
        source='show',
        queryset=Show.objects.all(),
    )

    class Meta:
        model = Attendance
        fields = ('participation', 'show', 'participation_id', 'show_id')


class FestivalSerializer(serializers.ModelSerializer):
    line_up = ShowSerializer(many=True)
    participants = ParticipationSerializer(many=True)

    class Meta:
        model = Festival
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'address', 'zip_code',
                  'city', 'line_up', 'participants')


class PartySerializer(serializers.ModelSerializer):
    festival = FestivalSerializer(required=False)
    festival_id = serializers.PrimaryKeyRelatedField(
        source='festival',
        queryset=Festival.objects.all(),
    )
    created_by = UserSerializer(default=CurrentUserDefault())

    class Meta:
        model = Party
        fields = ('id', 'name', 'created_by', 'festival', 'festival_id',)


class PartyInviteSerializer(serializers.ModelSerializer):
    party = PartySerializer(required=False)
    party_id = serializers.PrimaryKeyRelatedField(
        source='party',
        queryset=Party.objects.all(),
    )
    sender = ParticipationSerializer(required=False)
    sender_id = serializers.PrimaryKeyRelatedField(
        source='sender',
        queryset=Participation.objects.all(),
    )
    receiver = ParticipationSerializer()
    receiver_id = serializers.PrimaryKeyRelatedField(
        source='receiver',
        queryset=Participation.objects.all(),
    )

    class Meta:
        model = PartyInvite
        fields = ('party', 'party_id', 'sender', 'sender_id', 'receiver', 'receiver_id',)


class TaskSerializer(serializers.ModelSerializer):
    party = PartySerializer(required=False)
    party_id = serializers.PrimaryKeyRelatedField(
        source='party',
        queryset=Party.objects.all(),
    )
    assignee = ParticipationSerializer(required=False)
    assignee_id = serializers.PrimaryKeyRelatedField(
        source='assignee',
        queryset=Participation.objects.all(),
    )
    assignor = ParticipationSerializer()
    assignor_id = serializers.PrimaryKeyRelatedField(
        source='assignor',
        queryset=Participation.objects.all(),
    )

    class Meta:
        model = Task
        fields = ('party', 'party_id', 'assignee', 'assignee_id', 'assignor', 'assignor_id',)