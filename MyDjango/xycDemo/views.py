from django.shortcuts import render, HttpResponse
import json
from . import models
from rest_framework import status

from rest_framework import viewsets
from .serializer import  UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''查看，编辑用户的界面'''
    queryset = models.User.objects.all()
    serializer_class = UserSerializer





class singin_User(viewsets.ModelViewSet):
    # def get(self,request,format=None):
    #     user=models.User.objects.all()
    #     serializer=UserSerializer(user,many=True)
    #     return Response(serializer.data)
    # def post(self,request,format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
