from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



# router = routers.DefaultRouter()
# router.register(r'login',views.userloginView.as_view(),base_name='login')
# router.register(r'users',views.UserViewList.as_view(),base_name='user')
# 重要的是如下三行
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    path('userloginView/',views.userloginView.as_view(),name='userlogin'),
    path('user/', views.UserViewList.as_view(),name='user'),
    # url(r'^', include(router.urls)),
    url(r'^docs/', schema_view, name="docs"),
    # drf登录
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

#urlpatterns = format_suffix_patterns(urlpatterns)