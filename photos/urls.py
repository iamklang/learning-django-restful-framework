from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from photos import views

urlpatterns = patterns('photos.views',
    url(r'^v1/photos/$', views.PhotoViewSet.as_view()),
    url(r'^v1/photos/(?P<pk>[0-9]+)/$', views.PhotoViewList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)