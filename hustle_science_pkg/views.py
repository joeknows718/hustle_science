from django.shortcuts import render
from django.http import HttpResponse
from hustle_science_pkg.models import Category, Post, UserProfile, Comment, Image, UserProfile


def index(request):
	posts = Post.objects.latest(datetime)[:20]
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/index.html', context_dict )

def post_business(request):
	posts = posts.objects.filter(category__contains='business').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_tech(request):
	posts = posts.objects.filter(category__contains='tehnology').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_music(request):
	posts = posts.objects.filter(category__contains='music').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_fashion(request):
	posts = posts.objects.filter(category__contains='fashion').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_news(request):
	posts = posts.objects.filter(category__contains='news').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_art(request):
	posts = posts.objects.filter(category__contains='art').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_art(request):
	posts = posts.objects.filter(category__contains='art').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )

def post_culture(request):
	posts = posts.objects.filter(category__contains='culture').latest(datetime)
	context_dict = {'posts' : posts }
	return render(request, 'hustle_science/topic.html', context_dict )



