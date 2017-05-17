#-*- coding:utf8 -*-
from django.shortcuts import render

# Create your views here.
import pdb

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from demo import tasks

from django.contrib.auth import authenticate, login
from rest_framework import authentication
from rest_framework.request import Request

def foo(request):
    r = tasks.add.delay(2, 2)
    return HttpResponse(r.task_id)


def loginapp(request):
    print request.session.session_key
    user = authenticate(username='admin', password='123')
    if user is not None:
        if user.is_active:
            print request.session.save(), user.is_authenticated()

            login(request, user)
            return HttpResponse({"sessionid": request.session.session_key})
    return HttpResponse("ok")
# from django.contrib.sessions.backends.db import SessionStore

class testlogin(APIView):

    permission_classes = (AllowAny, )

    def post(self, request):

        print request.user, dir(request._request), type(request), request._request.META
        # pdb.set_trace()
        data = Response("ok")
        # print data.set_cookie("csrftoken")
        return data


class Login(APIView):

    permission_classes = (AllowAny, )

    def post(self, request):
        print "login===="
        user = authenticate(username='admin', password='admin')
        if user is not None:
            if user.is_active:
                print request.session.save(), user.is_authenticated()
                login(request, user)
                return Response({"sessionid": request.session.session_key})
        return Response("ok")
