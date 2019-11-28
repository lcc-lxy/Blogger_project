from django.conf.urls import url

from music import views

urlpatterns = [
    url(r'^player/(\w+)$',views.player),
    url(r'^search',views.search),
    url(r'^discuss',views.discuss),
    url(r'^player/up/(\w+)',views.up),
    url(r'^player/down/(\w+)',views.down),
]

