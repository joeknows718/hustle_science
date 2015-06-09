from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField



class Category(models.Model):
	tag = models.CharField(max_length=128, unique=True)
	def __unicode__(self): 
		return self.tag 

class UserProfile(models.Model):
	user =  models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	#roles
	about = models.TextField()

	def __unicode__(self):
		return self.username


class Post(models.Model):
	category = models.ManyToManyField(Category)
	title = models.CharField(max_length=128, unique=True)
	published = models.DateField() #defined in view as UTC converted client side w/ moment.js
	author = models.ForeignKey(User)
	featured_image = models.ImageField(upload_to='featured_img', blank=False)
	body = RichTextField(config_name='awesome_ckeditor')
	video_iframe = models.URLField(max_length=200)
	project_iframe = models.URLField(max_length=200)

	def __unicode__(self):
		return self.title 


class Comment(models.Model):
	article = models.ForeignKey(Post)
	comment_text = models.TextField()
	published = models.DateTimeField()
	username = models.CharField(max_length=145)

	def __unicode__(self):
		return self.comment_text


class  Image(models.Model):
	post =  models.ForeignKey(Post)
	image = models.ImageField(upload_to='slideshow images')




