"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
##from yellow_line.views import *

##urlpatterns = [
##    url(r'^$', 'django.contrib.auth.views.login'),
##    url(r'^logout/$', views.logout_page),
##    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
##    url(r'^register/$', views.register),
##    url(r'^register/success/$', views.register_success),
##    url(r'^home/$', views.home),
##]

urlpatterns = [
    url(r'^yellow_line/', include('yellow_line.urls', namespace="yellow_line")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^yellow_line/admin/',admin.site.urls),
    url(r'^$', include('yellow_line.urls'))
]
