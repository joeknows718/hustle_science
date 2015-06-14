from django.shortcuts import render
from django.http import HttpResponse
from hustle_science_pkg.models import Category, Post, UserProfile, Comment, Image, UserProfile


def index(request):
	posts = Post.objects.latest(datetime)[:20]
	featured_posts = Post.objects.filter(featured=True).latest(datetime)[:2]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/index.html', context_dict )

def post_business(request):
	posts = Posts.objects.filter(category__contains='business').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='business').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_tech(request):
	posts = Posts.objects.filter(category__contains='tehnology').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='tehnology').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_music(request):
	posts = Posts.objects.filter(category__contains='music').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='music').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_fashion(request):
	posts = Posts.objects.filter(category__contains='fashion').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='fashion').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_news(request):
	posts = Posts.objects.filter(category__contains='news').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='news').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_art(request):
	posts = Posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = Posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_art(request):
	posts = posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = posts.objects.filter(category__contains='art').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_culture(request):
	posts = posts.objects.filter(category__contains='culture').latest(datetime)
	featured_posts = posts.objects.filter(category__contains='culture').latest(datetime)
	featured_posts = featured_posts.objects.filter(featured=True).latest(datetime)[:1]
	context_dict = {'posts' : posts, featured_posts='featured_posts' }
	return render(request, 'hustle_science/topic.html', context_dict )



