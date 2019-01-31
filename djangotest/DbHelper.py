from django.http import HttpResponse, JsonResponse
import json
from TestModel.models import MyApp


def insert(request, name):
    if 'name' in request.GET:
        try:
            m = MyApp(name=request.GET['name'])
            m.save()
            return HttpResponse('insert ok')
        except Exception:
            return HttpResponse('insert error')
    else:
        return HttpResponse(r'id is not found')


def select(request):
    if 'name' in request.GET:
        try:
            list = []
            res = MyApp.objects.get(name=request.GET['id'])
            return HttpResponse(res.id)
        except Exception:
            return HttpResponse('insert error' + Exception.args)
    else:
        return HttpResponse(r'id is not found')


def userDefault(obj):
    return {
        "status": obj.status,
        "data": obj.data
    }


def getAll(request):
    class User:
        status = 0
        data = []
    res = MyApp.objects.all()
    u = User()
    u.status = 1
    for v in res:
        u.data.append({"name": v.name, "psw": v.psw})
    return HttpResponse(json.dumps(u, default=userDefault))


def insert2(request, name, psw):
    m = MyApp()
    m.name = name
    m.psw = psw
    m.save()
    return HttpResponse('insert ok')
