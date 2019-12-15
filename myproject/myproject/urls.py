from django.conf.urls import include, url
from django.contrib import admin
#from rest_framework.urlpatterns import format_suffix_patterns
#from myapp import views
from rest_framework import routers

#import myapp,polls



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^employees/', include('myapp.urls')),
     url(r'^poll/', include('polls.urls')),
    #url(r'^employees/', myapp.views.employeeList.as_view()),
    #url(r'^employees/(?P<pk>\d+)', myapp.views.employeeList.as_view({'get': 'list', 'post': 'create'})),
    #url(r'^MoviesList/$', views.MoviesListSerializers.as_view()),
]
