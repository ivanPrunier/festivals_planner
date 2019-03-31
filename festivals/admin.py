from django.contrib import admin

from festivals.models import Artist, Stage, Show, Festival, Participation, Attendance


class ArtistAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'infoconcert_url',)


class FestivalAdmin(admin.ModelAdmin):
    fields = ('infoconcert_url',)


class ShowAdmin(admin.ModelAdmin):
    fields = ('festival', 'artist', 'stage', 'name', 'start_datetime', 'end_datetime',)


class StageAdmin(admin.ModelAdmin):
    fields = ('festival', 'name', 'description',)


class ParticipationAdmin(admin.ModelAdmin):
    fields = ('festival', 'user', 'start_date', 'end_date')


class AttendanceAdmin(admin.ModelAdmin):
    fields = ('participation', 'show',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Participation, ParticipationAdmin)
admin.site.register(Attendance, AttendanceAdmin)
