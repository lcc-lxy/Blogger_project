"""shanzhaimusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from shanzhaimusic import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/',include('users.urls')),

    url(r'^index/$',views.index),
    url(r'^index/message',views.message),
    url(r'^index/exit',views.exit),
    url(r'^index/index_server',views.index_server),

    url(r'^musician/',include('musician.urls')),
    url(r'^music/',include('music.urls')),

    url(r'^personal/',include('person.urls')),

]

# 3, 配置 绑定 media_url 和 media_root 显性操作
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


