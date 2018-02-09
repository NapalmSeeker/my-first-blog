from django.conf.urls import url
from . import views

app_name = 'store'

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', views.prod_detail, name='prod_detail'),
    url(r'^$', views.store_index, name='store_index'),
]