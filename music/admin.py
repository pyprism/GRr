from django.contrib import admin
from music.models import Playlist
# Register your models here.

class PlaylistAdmin(admin.ModelAdmin):
	list_display = ('songName','favorite')
	search_fields = ('songName' ,)

admin.site.register(Playlist,PlaylistAdmin)