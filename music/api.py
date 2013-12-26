from tastypie.resources import ModelResource
from music.models import Playlist
from music.scrap import alphaSelect
class EntryResource(ModelResource):
    class Meta:
        queryset = Playlist.objects.all()
        queryset = alphaSelect
        resource_name = 'playlist'