from django.http import HttpResponse
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
from . import redis


class CommonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        if redis.IpMiddleware(ip):
            pass
        else:
            return HttpResponse("请求过快")

    def process_response(self, request, response):
        return response
