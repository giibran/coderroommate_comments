from django.conf.urls import patterns, url
from my_app import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create_comment/$', views.CommentCreateView.as_view(),
        name='create_comment'),
)
