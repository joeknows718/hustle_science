from django.conf.urls import patterns, url 
from hustle_science_pkg import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^posts-business/', views.post_business, name='/posts-business' ),
	url(r'^posts-technology/', views.post_tech, name='/posts-technology' ),
	url(r'^posts-fashion/', views.post_fashion, name='/posts-fashion' ),
	url(r'^posts-music/', views.post_music, name='/posts-music' ),
	url(r'^posts-art/', views.post_art, name='/posts-art' ),
	url(r'^posts-news/', views.post_news, name='/posts-news' ),
	url(r'^posts-culture/', views.post_culture, name='/posts-culture' ),
	url(r'^about/', views.about, name='/about' ),
	url(r'^team/', views.team, name='/team' ),
	)
	
