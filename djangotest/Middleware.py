from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from . import redis


# 中间件
class CommonMiddleware(MiddlewareMixin):
    def process_request(self, request):  # request
        # 获取ip
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        # false拦截
        if redis.IpMiddleware(ip):
            pass
        else:
            return HttpResponse("请求过快")

    def process_response(self, request, response):
        return response  # 不做处理，原样输出
