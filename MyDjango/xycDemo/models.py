import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    nickName=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    Modify_time=models.DateTimeField(auto_now=True)
    phoneNumber=models.CharField(max_length=11,unique=True)
    username=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    sex=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    def __str__(self):
        smart_str = '%s%s%s%s%s%s' % (self.phoneNumber, self.nickName, self.age, self.sex, self.username, self.password)
        return smart_str
