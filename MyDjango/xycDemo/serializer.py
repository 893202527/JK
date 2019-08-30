from django.contrib.auth.models import User,Group
from  rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ordering = ['id']
        #depth=1  查询层1,2,3
        fields = '__all__'
        # 除了nid都查
        # exclude = ['nid']

class userlogin(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('phoneNumber','password')
        extra_kwargs = {'password': {'write_only': True}}
        # read_only_fields =['phoneNumber']


class userInformation(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('nickName','phoneNumber','username','age')