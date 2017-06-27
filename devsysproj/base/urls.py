#-*- coding:utf8 -*-

from django.conf.urls import url

from baseview import OperationView

urlpatterns = [
    url(r'^(?P<app_name>[^/]*)/(?P<model_name>[^/]*)/op/(?P<op_name>[^/]*)$', OperationView.as_view()),  #操作
]
