from  django.http import HttpResponse


def index(requset):
    return HttpResponse('Django 测试')