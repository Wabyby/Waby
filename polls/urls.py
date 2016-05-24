from django.conf.urls import url

from polls.Views import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user>[0-9]+)/$', views.detail, name='detail'),
]