from django.contrib import admin

from festivals.models import Artist, Stage, Show, Festival


class ArtistAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)


class FestivalAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'start_date', 'end_date', 'address', 'zip_code', 'city',)


class ShowAdmin(admin.ModelAdmin):
    fields = ('festival', 'artist', 'stage', 'name', 'start_datetime', 'end_datetime',)


class StageAdmin(admin.ModelAdmin):
    fields = ('festival', 'name', 'description',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Stage, StageAdmin)
