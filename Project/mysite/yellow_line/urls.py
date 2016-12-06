from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'display/name/$',views.displayname,name='displayname'),
    url(r'display/date/$',views.displaydate,name='displaydate'),
    url(r'display/venue/$',views.displayvenue,name='displayvenue'),
    url(r'display/category/$',views.displaycategory,name='displaycategory'),
    url(r'search/(?P<a>[Art,Food,Music,Shopping,Theatre]+)/',views.searchcategory,name='searchcategory')
    ]
