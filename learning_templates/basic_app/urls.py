from django.conf.urls import url, include
from basic_app import views

#template tagging
app_name = 'basic_app' #this tells django to look for basic_app and find url that matches

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
