from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),

    # /blog/sum/1234567890/
    url(r'^sum/(?P<x>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
]
