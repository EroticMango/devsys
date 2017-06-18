#-*- coding:utf8 -*-

from django.conf.urls import url

from baseview import OperationBaseView

urlpatterns = [
    url(r'^(?P<app_name>[^/]*)/(?P<model_name>[^/]*)/op/(?P<op_name>[^/]*)$', OperationBaseView.as_view()),  #增加
#     url(r'^(?P<app_name>[^/]*)/(?P<model_name>[^/]*)/op/add$', api.SignUpApi.as_view()),  #增加
]
