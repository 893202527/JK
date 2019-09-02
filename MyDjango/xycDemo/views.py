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

from rest_framework.renderers import JSONRenderer


def msg(status,data):
    msg={
        'status':status,
        'data':data,
    }
    return  msg


class userloginView(generics.GenericAPIView):
    """用户登陆"""
    queryset = models.User.objects.all()
    serializer_class = serializer.userlogin

    # lookup_field = 'phoneNumber'
    def post(self, request, *args, **kwargs):

        userlogin=models.User.objects.filter(phoneNumber=request.data.get('phoneNumber'),password=request.data.get('password'))
        u=models.User.objects.get(phoneNumber=request.data.get('phoneNumber'))


        if not  userlogin:
            return Response(msg('用户不存在',None),status=status.HTTP_200_OK)
        elif u.password != request.data.get('password'):
            return Response(msg('请检查账号密码是否一致',None),status=status.HTTP_200_OK)
        else:
            data=models.User.objects.filter(phoneNumber=request.data.get('phoneNumber')).first()
            # print(type(data))
            s=serializer.userlogin(data=request.data,many=False)#一条数据False
            print(type(s))
            s.is_valid(raise_exception=True)

            return Response(s.data,status=status.HTTP_200_OK)
            # else:
            #     return Response(s.errors)



class UserViewList(generics.GenericAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.userlogin
    def get(self, request, *args, **kwargs):
        """获取用户"""
        print('进入get请求')
        return self.retrieve(request,*args, **kwargs)
    def post(self, request, *args, **kwargs):
        """创建用户"""
        print('进入post请求')
        queryset=UserSerializer(data=request.data)
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
