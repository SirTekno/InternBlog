from django.conf.urls import patterns, url

from . import views

urlpatterns=[
    url(r'^post/(?P<slug>[0-9A-Za-z-_.//]+)/$', views.post, name='post'),
    url(r'^$', views.index, name='index')
]
