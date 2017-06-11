#-*- coding:utf8 -*-

from rest_framework.response import Response

def handle_response_data(*args, **kwargs):
    data = kwargs.pop('data', None)
    return_dict = {
        'code': kwargs.pop('code', 200),
        'msg': kwargs.pop('msg', 'ok')
    }
    if data is not None:
        return_dict['data'] = data

    return Response(
                    status=200,
                    data=return_dict)


def form_error(errors_dict):

    if errors_dict.has_key('non_field_errors'):
        msg = errors_dict['non_field_errors'][0]
        return handle_response_data(code=420, msg=msg)

    message = None
    for k,v in errors_dict.iteritems():
        if message is None:
            message = u'%s:%s' %(k, v[0])

    return handle_response_data(code=412, msg=msg)
