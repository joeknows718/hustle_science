from django.conf.urls import patterns, url 
from hustle_science_pkg import views
from hustle_science_pkg.views import PostView, HomeView, TagView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='index'),
	url(r'^(?P<tag>[a-zA-Z0-9-]+)/$', TagView.as_view(), name = 'tagged_view'),
	url(r'^(?P<tag>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)$', PostView.as_view(), name = 'tagged_view'),
	url(r'^about/', views.about, name='/about' ),
	url(r'^team/', views.team, name='/team' ),
	)
	
