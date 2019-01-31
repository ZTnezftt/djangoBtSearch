"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import view
from . import HelloWorld
from . import db
from . import DbHelper
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/a', view.hello),
    path('hello', HelloWorld.hello),
    path('insert', db.testdb),
    path('select', db.getDb),
    path('s', db.g),
    path('insertDb', DbHelper.insert),
    path("selectDb", DbHelper.select),
    path('insert2/<name>/<psw>', DbHelper.insert2),
    path('getAll', DbHelper.getAll),
    path('torrent/<name>/<sort>/<page>', view.parseTorrent)
]