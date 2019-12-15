from django.conf.urls import  url
from . import views
#from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.models import User
from polls import views
from .views import polls_list,polls_detail,PollList,PollDetail,ChoiceList,CreateVote, PollpublicSet
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views
from polls import views
app_name='polls'
urlpatterns = [
 url(r'^poll/$', views.polls_list, name='polls_list'),

 #url(r'^ObtainExpiringAuthToken/$', views.ObtainExpiringAuthToken, name='ObtainExpiringAuthToken'),

 url(r'^polls_detail/(?P<id>[0-9]+)/', views.polls_detail, name ='polls_detail'),
# ####################APIView################
 url(r'^PollList/$', views.PollList.as_view(), name='PollList'),
 url(r'^LoginView/$', views.LoginView.as_view(), name='login'),
 url(r'^PollDetail/(?P<id>[0-9]+)/', views.PollDetail.as_view()),

#
# #########################generics#################
 url(r'^PollListgenerics/$', views.PollListgenerics.as_view(), name='PollListgenerics'),
 url(r'^PollDetailgenerics/(?P<id>[0-9]+)/', views.PollDetailgenerics.as_view()),
 url(r'^ChoiceList/$', views.ChoiceList.as_view(), name='ChoiceList'),
#
 url(r'^CreateVote/$', views.CreateVote.as_view(), name='CreateVote'),
#
 url(r'^ProductList/$', views.ProductList.as_view(), name='ProductList'),
# ###################viewsets################
 url(r'^user_list/$', views.UserViewSet.as_view({'get': 'list'})),
#
# ################ModelViewSet#################################
 url(r'^PollViewSet/$', views.PollViewSet.as_view({'get': 'list', 'post': 'create'}), name='PollViewSet'),
#
# #####################################ModelViewSet#################################
 url(r'^PollpublicSet/$', views.PollpublicSet.as_view({'get': 'list', 'post': 'create'}), name='PollpublicSet'),
#
#
#
#
# url(r'^particle_list/$', views.particle_list, name='particle_list'),

url(r'^voterlist/', views.voterlist.as_view()),

url(r'^voter1list/', views.voter1list.as_view()),
]
