from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = "videodownloader"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^downloadfile/$', views.downloadfile, name='downloadfile'),
]
