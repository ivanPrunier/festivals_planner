from django.contrib import admin

from festivals.models import Artist, Stage, Show, Festival


class ArtistAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'infoconcert_url',)


class FestivalAdmin(admin.ModelAdmin):
    fields = ('infoconcert_url',)


class ShowAdmin(admin.ModelAdmin):
    fields = ('festival', 'artist', 'stage', 'name', 'start_datetime', 'end_datetime',)


class StageAdmin(admin.ModelAdmin):
    fields = ('festival', 'name', 'description',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Stage, StageAdmin)
