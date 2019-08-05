from django.shortcuts import render, HttpResponse
import json
from . import models
from rest_framework import viewsets
from .serializer import  UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializer
# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from  .  import serializer
from rest_framework.parsers import FormParser, MultiPartParser


class userloginView(generics.GenericAPIView,mixins.RetrieveModelMixin):
    """用户登陆"""


    serializer_class = serializer.userlogin
    lookup_field = 'phoneNumber'
    def post(self, request, *args, **kwargs):
        # userlogin=models.User.objects.get(phoneNumber=request.POST.get('phoneNumber'))
        # print(userlogin)
        queryset = serializer.userlogin(data=request.POST)
        print(queryset)
        print(queryset.is_valid())
        if queryset.is_valid():
            return Response(queryset.data,status=status.HTTP_200_OK)
        else:
            return Response(queryset.errors,status.HTTP_400_BAD_REQUEST)



class UserViewList(generics.GenericAPIView,mixins.RetrieveModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.userlogin
    def get(self, request, *args, **kwargs):
        """获取用户"""
        print('进入get请求')
        return self.retrieve(request,*args, **kwargs)



    def post(self, request, *args, **kwargs):
        """创建用户"""
        print('进入post请求')
        queryset=UserSerializer(data=request.POST)
        if  queryset.is_valid():
            queryset.save()

            msg={
                'msg':'创建成功',
                'code':'1'
            }
            return Response(data=msg,status=status.HTTP_201_CREATED)
        return Response(queryset.error_messages,status=status.HTTP_400_BAD_REQUEST)




# class singin_User(viewsets.ModelViewSet):
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



    # def register_user(requsert):
    #     if requsert.method == 'POST' and requsert.POST:
    #         phoneNumber = requsert.POST.get('phoneNumber')
    #         if models.User.objects.filter(phoneNumber=phoneNumber) != None:
    #             nickName = requsert.POST.get('nickname')
    #             username = requsert.POST.get('username')
    #             sex = requsert.POST.get('sex')
    #             age = requsert.POST.get('age')
    #             password = requsert.POST.get('password')
    #
    #             user = models.User(nickName=nickName, password=password, username=username, sex=sex, age=age,
    #                                phoneNumber=phoneNumber)
    #
    #             user.save()
    #             msg = {'msg': 'successful', 'msg_code': '1'}
    #             return HttpResponse(json.dumps(msg), content_type='application/json;charset=utf-8')
    #         else:
    #             msg = {'msg': '已注册', 'msg_code': '1001'}
    #             return HttpResponse(json.dumps(msg), content_type='application/json;charset=utf-8')
    #     else:
    #         msg = {'msg': '请求方式错误', 'msg_code': '2002'}
    #         return HttpResponse(json.dumps(msg), content_type='application/json;charset=utf-8')
