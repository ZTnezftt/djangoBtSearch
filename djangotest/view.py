from django.http import HttpResponse
from . import soup
import json
import redis
def hello(request):
    return HttpResponse("Hello world ! ")


def parseTorrent(request, name, sort, page):
    return HttpResponse(soup.parse(json.loads(soup.init())['data'][0], name, sort, page))


