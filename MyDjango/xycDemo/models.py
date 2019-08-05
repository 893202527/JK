import datetime

from django.db import models
import json
from django.utils import timezone
# Create your models here.


class User(models.Model):
    nickName=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    Modify_time=models.DateTimeField(auto_now=True)
    phoneNumber=models.CharField(max_length=11,unique=True)
    username=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    sex =(
        ('male','男'),
        ('female','女'),)
    password=models.CharField(max_length=100)

    def __str__(self):
        smart = {'phoneNumber':self.phoneNumber,
                 'nickName':self.nickName,
                 'age':self.age,
                 'sex':self.sex,
                 'username':self.username
                }

        return json.dumps(smart)

class user_info(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    ip=models.CharField(max_length=100)
    login_time=models.DateTimeField(auto_now=True)
    login_times=models.IntegerField(auto_created=True)#实现自增,AUTO_INCREMENT=100从100开始自增



