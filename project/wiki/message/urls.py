from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^/(?P<topic_id>\w{1,11})$',views.message)

]