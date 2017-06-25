from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.blogpost_detail , name='blogpost_detail')
]
