from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510, blank=True, null=True)
    infoconcert_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Festival(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    infoconcert_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510, blank=True, null=True)

    def __str__(self):
        return self.name


class Show(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name='line_up')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tour')
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='shows', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.artist} at {self.festival}'


class Party(models.Model):
    name = models.CharField(max_length=255)
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class Participation(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, related_name='members', null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


class PartyInvite(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='invites')
    receiver = models.ForeignKey(Participation, on_delete=models.CASCADE, related_name='pending_invites')
    sender = models.ForeignKey(Participation, on_delete=models.CASCADE, related_name='sent_invitations')
    accepted = models.BooleanField(default=False)


class Task(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='checklist_items')
    assignee = models.ForeignKey(Participation, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_tasks')
    assignor = models.ForeignKey(Participation, on_delete=models.SET_NULL, blank=True, null=True, related_name='given_tasks')


class Attendance(models.Model):
    participation = models.ForeignKey(Participation, on_delete=models.CASCADE, related_name='shows')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='attendants')
