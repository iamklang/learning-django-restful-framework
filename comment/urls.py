from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from comment import views


urlpatterns = patterns('comment.views',
    url(r'^v1/comments/$', views.Comments.as_view()),
    url(r'^v1/comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)