#-*- coding:utf8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.apps import apps


class OperationBaseView(APIView):

    permission_classes = (AllowAny, )

    def dispatch(self, request, *args, **kwargs):
        """
        `.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        扩展APIView， 根据操作方法来加载handle
        """
        self.args = args
        self.kwargs = kwargs
        # print "args=========", self.args, "kwargs=========", self.kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?
        try:
            self.initial(request, *args, **kwargs)
            # Get the appropriate handler method
            handler = self.http_method_not_allowed
            if request.method.lower() in self.http_method_names:
                app_name = kwargs['app_name']
                model_name = kwargs['model_name']
                model = apps.get_model(app_name, model_name)
                op_name = kwargs['op_name']
                op_name = ''.join([op_name[0].capitalize(), op_name[1:]])
                op = getattr(model, op_name, None)
                if op is not None:
                    handler = getattr(op(), request.method.lower(),
                                      self.http_method_not_allowed)
                # handler = getattr(self, request.method.lower(),
                #                   self.http_method_not_allowed)

            response = handler(request, *args, **kwargs)

        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(
            request, response, *args, **kwargs)
        return self.response


class OperationView(OperationBaseView):
    '''
        针对登录用户操作
    '''
    permission_classes = (IsAuthenticated, )
