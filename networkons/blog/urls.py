from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),

    # /blog/sum/1234567890/
    url(r'^sum/(?P<numbers>[/\d]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
]
