#-*- coding:utf8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from base.response import handle_response_data, form_error

from django.contrib.auth import authenticate, login

from accounts.forms.postemailurlform import PostEmailUrlForm

class PostEmailUrlApi(APIView):

    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        form_data = PostEmailUrlForm(data=request.POST.copy())
        if form_data.is_valid():
            data = form_data.data
            form_data.send_email()
            return handle_response_data()
        else:
            return form_error(form_data.errors)
