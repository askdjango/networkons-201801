from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.field_list),
    url(r'^field2/$', views.field_list2),
    url(r'^record/$', views.record_list),
    url(r'^record/(?P<pk>\d+)/$', views.record_detail),
]

