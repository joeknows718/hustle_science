from django.contrib import admin
from hustle_science_pkg.models import Category, Post, UserProfile, Comment, Image, UserProfile

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(UserProfile)

# Register your models here.
