from django.conf.urls import patterns, url 
from hustle_science_pkg import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	)