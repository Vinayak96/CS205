from django.conf.urls import url
from . import views   
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'displayname.html',views.displayname,name='displayname'),
    url(r'displaydate.html',views.displaydate,name='displaydate'),
    url(r'displayvenue.html',views.displayvenue,name='displayvenue'),
    url(r'displaycategory.html',views.displaycategory,name='displaycategory'),
    url(r'search/(?P<a>[\w ]+).html',views.searchcategory,name='searchcategory'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    ]
