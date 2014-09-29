from django.conf.urls import include, url
from django.contrib import admin
from myassignment import rest_api

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/users/$', rest_api.UserViewSet.as_view()),
    url(r'^v1/users/(?P<pk>[0-9]+)/$', rest_api.UserViewList.as_view()),
    url(r'^', include('comment.urls')),
    url(r'^', include('photos.urls')),
]
