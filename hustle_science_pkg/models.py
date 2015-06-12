from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.template.defaultfilters import slugify



class Category(models.Model):
	tag = models.CharField(max_length=128, unique=True)
	def __unicode__(self): 
		return self.tag 

class Content_Type(models.Model):
	media_type = models.CharField(max_length=128, unique=True)
	def __unicode__(self):
		return self.media_type

class UserProfile(models.Model):
	user =  models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	#roles
	about = models.TextField()

	def __unicode__(self):
		return self.username


class Post(models.Model):
	category = models.ManyToManyField(Category)
	content_type = ForeignKey(Content_Type)
	title = models.CharField(max_length=128, unique=True, blank=False)
	published = models.DateField() #defined in view as UTC converted client side w/ moment.js
	author = models.ForeignKey(User)
	featured_image = models.ImageField(upload_to='featured_img', blank=False)
	body = RichTextField(config_name='awesome_ckeditor', blank=False)
	media_iframe = EmbedVideoField(max_length=200, null=True, blank=True)
	project_url = models.URLField(max_length=200, null=True, blank=True)
	featured = models.BooleanField(default=False)
	screenshot = models.ImageField(upload_to="app_screenshots", null=True, blank=True )
	slug = models.SlugField(unique=True, default='')

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

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




