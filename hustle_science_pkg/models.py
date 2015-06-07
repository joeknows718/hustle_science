from django.db import models
from django.contrib.auth.models import User 

class Category(models.Models):
	tag = models.charField(max_length=128, unique=True)
	def __unicode__(self): 
		return self.tag 

class UserProfile(model.Models):
	user =  models.OnetoOne(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	#roles
	about = models.TextAreaField

	def __unicode__(self):
		return self.username


class Post(model.Models):
	category = models.ManyToManyField(Category)
	title = models.CharField(max_length=128, unique=True)
	published = models.DateField() #defined in view as UTC converted client side w/ moment.js
	author = models.ForeignKey(User)
	featured_image = ImageField(upload_to='featured_images', blank=False)
	body = models.TextAreaField()
	video_iframe = models.URLField(max_length=200)
	project_iframe = models.URLField(max_length=200)
	code_text = TextAreaField()

	def __unicode__(self):
		return self.title 


class Comment(model.Models):
	article = models.ForeignKey(Posts)
	comment_text = models.CharField(max_length=255)
	published = models.DateTimeField()
	username = models.CharField()

	def __unicode__(self):
		return self.comment_text


class  Images(model.Models):
	post =  ForeignKey(Posts)
	image = models.ImageField(upload_to='slideshow images')




