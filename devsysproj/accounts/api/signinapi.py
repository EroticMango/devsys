#-*- coding:utf8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from accounts.forms.signinform import SignInForm

from base.response import handle_response_data, form_error

from django.contrib.auth import authenticate, login

from django.conf import settings

from accounts.models.myuser import MyUser
from accounts.serializer.signinserializer import SignInSerializer

class SignInApi(APIView):

    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        form_data = SignInForm(data=request.POST.copy())
        if form_data.is_valid():

            credentials = form_data.data
            user = authenticate(**credentials)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    myuser = MyUser.objects.get(user=user)
                    signinserializer = SignInSerializer(myuser)
                    return handle_response_data(data=signinserializer.data)
            return handle_response_data(code=420, msg=u'用户不存在或者密码错误')
        else:
            return form_error(form_data.errors)
