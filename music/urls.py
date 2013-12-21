from django.conf.urls import patterns, url
from music import views

urlpatterns = patterns('',
        url(r'^$', views.alphaSelect, name='index'),
        url(r'^hiren/', views.alphaSelect)
        )