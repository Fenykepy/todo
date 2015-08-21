#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.urlpatterns import format_suffix_patterns

from task import views


urlpatterns = [

        url(r'^$', views.TaskList.as_view(),
            name="task-list"),
        url(r'^(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(),
            name="task-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


# To get static files during development
urlpatterns += staticfiles_urlpatterns()
