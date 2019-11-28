from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.users),
    # http://127.0.0.1:8000/v1/users/<username>
    url(r'^/(?P<username>\w{1,11})$',views.users),
    url(r'^/(?P<username>\w{1,11})/avatar$',views.users_avatar),
    #http://127.0.0.1:8000/v1/users/weibo/url
    url(r'^/weibo/url',views.users_weibo_url)
]