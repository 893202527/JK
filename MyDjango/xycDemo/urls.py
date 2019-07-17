from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin
from  rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet,base_name='user')
router.register(r'groups',views.GroupViewSet,base_name='group')


# 重要的是如下三行
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


urlpatterns = [
    # path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('register_user/', views.register_user, name='register_user'),
    #path('UserViewSet/',views.UserSerializer,name='UserViewSet'),


    url(r'^docs/', schema_view, name="docs"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # drf登录
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]