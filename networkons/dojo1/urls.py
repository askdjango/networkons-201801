from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.field_list),
    url(r'^field2/$', views.field_list2),
]

