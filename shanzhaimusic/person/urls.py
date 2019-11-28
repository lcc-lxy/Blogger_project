from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^diary$',views.diary),
    url(r'^photo$',views.photo),
    url(r'^handle_photo$',views.handle_photo),
    url(r'^handle_index',views.handle_index),
    url(r'^username$',views.username),
    url(r'^info$',views.info),
]