#-*- coding:utf8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated

from accounts.forms.signupform import SignUpForm

from base.response import handle_response_data, form_error

class SignUpApi(APIView):

    permission_classes = (AllowAny, )

    def post(self, request, format=None):

        form_data = SignUpForm(data=request.POST.copy())
        if form_data.is_valid():
            user = form_data.create(form_data.data)
            return handle_response_data()
        else:
            return form_error(form_data.errors)
