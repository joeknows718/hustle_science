from django.shortcuts import render
from django.http import HttpResponse
from hustle_science_pkg.models import Category, Post, UserProfile, Content_Type, Image, UserProfile
from django.core.mail import send_mail
from django.generic.views import View
from forms import ContactForm 
from django.conf import settings


class HomeView(View):

	def get(self, request):
		tag = request.tag
		context_dict = {}
		posts = Post.objects.order_by('-published')[:20]
		featured_posts = Post.objects.filter(featured=True).order_by('-published')[:2]
		context_dict['posts'] = posts
		context_dict['featured_posts'] = featured_posts
		return render(request, 'index.html', context_dict )

class TagView(View):

	def get(self, request):
		tag = self.kwargs.get('slug', None)
		context_dict = {}
		posts = Post.objects.filter(category__tag__in=tag).order_by('-published')[:20]
		featured_posts = posts.filter(featured=True).order_by('-published')[:2]
		context_dict['posts'] = posts
		context_dict['featured_posts'] = featured_posts
		return render(request, 'index.html', context_dict )

class PostView(View):

	def get(self, request):
		
		context_dict = {}
		posts = Post.objects.order_by('-published')[:20]
		featured_posts = Post.objects.filter(featured=True).order_by('-published')[:2]
		context_dict['posts'] = posts
		context_dict['featured_posts'] = featured_posts
		return render(request, 'index.html', context_dict )

class StaticView(View):

	def about(self, request):
		#Static page
		return render(request, 'hustle_science/about.html')

	def team(self, request):
		context_dict = {}
		user = UserProfile.objects.all()
		context_dict['users'] = user
		return render(request, 'hustle_science/team.html', context_dict)

class ContactView(FormView):

	form_class = ContactForm
	template = 'contact.html'
	success_url = '/email-sent/'


	def form_valid(self, form):

		name = form.cleaned_data.get('name')
		message_text = form.cleaned_data.get('body')
		subject = form.cleaned_data.get('subject')
		email = form.cleaned_data.get('email')

		message = message_text + ' - ' + name + ' @ ' + email 

		send_mail(subject=subject, message=message, 
				from_email='info@movesmade.com', 
				recipient_list=[settings.ADMINS])

	return super(ContactFormView, self).form_valid(form)



