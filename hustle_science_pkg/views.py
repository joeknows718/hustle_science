from django.shortcuts import render
from django.http import HttpResponse
from hustle_science_pkg.models import Category, Post, UserProfile, Comment, Image, UserProfile


def index(request):
	context_dict = {}
	posts = Post.objects.latest(datetime)[:20]
	featured_posts = Post.objects.filter(featured=True).latest(datetime)[:2]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/index.html', context_dict )

def post_business(request):
	context_dict = {}
	posts = Posts.objects.filter(category__contains='business').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='business').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )

def post_tech(request):
	context_dict = {}
	posts = Posts.objects.filter(category__contains='tehnology').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='tehnology').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )

def post_music(request):
	context_dict = {}
	posts = Posts.objects.filter(category__contains='music').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='music').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )

def post_fashion(request):
	context_dict = {}
	posts = Posts.objects.filter(category__contains='fashion').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='fashion').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )

def post_news(request):
	context_dict = {}
	posts = Posts.objects.filter(category__contains='news').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='news').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )

def post_art(request):
	context_dict = {}
	posts = Posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )

def post_art(request):
	context_dict = {}
	posts = posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )

def post_culture(request):
	context_dict = {}
	posts = posts.objects.filter(category__contains='culture').latest(datetime)
	featured_posts = posts.objects.filter(category__contains='culture').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict['posts'] = posts
	context_dict['featured_posts'] = featured_posts
	return render(request, 'hustle_science/topic.html', context_dict )


def about(request):
	#Static page
	return render(request, 'hustle_science/about.html')

def team(request):
	context_dict = {}
	user = UserProfile.objects.all()
	context_dict['users'] = user
	return render(request, 'hustle_science/team.html', context_dict)
