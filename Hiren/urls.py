from django.conf.urls import patterns, include, url
from music.api import EntryResource

from django.contrib import admin
admin.autodiscover()

entry_resource = EntryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hiren.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('music.urls')),
    (r'^api/', include(entry_resource.urls)),
)
