#-*- coding:utf8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from accounts.forms.signinform import SignInForm

from base.response import handle_response_data, form_error

from django.contrib.auth import authenticate, login

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
                    return_data = {
                        'sessionid': request.session.session_key
                    }
                    return handle_response_data(data=return_data)
            return handle_response_data(code=420, msg=u'用户不存在或者密码错误')
        else:
            return form_error(form_data.errors)

