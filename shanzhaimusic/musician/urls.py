from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.musician),
    url(r'^musician$', views.musician),
    url(r'^musician_lx$', views.musician_lx),
    url(r'^musician_yg$', views.musician_yg),
    url(r'^musician_dz$', views.musician_dz),
    url(r'^musician_my$', views.musician_my),
    url(r'^musician_js$', views.musician_js),
]
