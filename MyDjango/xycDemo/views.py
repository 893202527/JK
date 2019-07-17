from django.shortcuts import render, HttpResponse
import json
from . import models

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import  UserSerializer, GroupSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''查看，编辑用户的界面'''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''查看，编辑组的界面'''
    queryset = Group
    serializer_class = GroupSerializer


def index(request):
    latest_question_list = models.Question.objects.order_by()
    print(latest_question_list)
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def register_user(requsert):
    if requsert.method == 'POST' and requsert.POST:

        phoneNumber = requsert.POST.get('phoneNumber')
        if models.User.objects.filter(phoneNumber=phoneNumber) != None:
            nickName = requsert.POST.get('nickname')
            username = requsert.POST.get('username')
            sex = requsert.POST.get('sex')
            age = requsert.POST.get('age')
            password = requsert.POST.get('password')

            user = models.User(nickName=nickName, password=password, username=username, sex=sex, age=age,
                               phoneNumber=phoneNumber)
            user.save()
            msg = {'msg': 'successful', 'msg_code': '1'}
            return HttpResponse(json.dumps(msg), content_type='application/json;charset=utf-8')
        else:
            msg = {'msg': '已注册', 'msg_code': '1001'}
            return HttpResponse(json.dumps(msg), content_type='application/json;charset=utf-8')
    else:
        msg = {'msg': '请求方式错误', 'msg_code': '2002'}
        return HttpResponse(json.dumps(msg), content_type='application/json;charset=utf-8')
