from django.conf.urls import patterns, include, url
from django.contrib import admin, auth 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hustle_science.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url('^', include('django.contrib.auth.urls')),
    url('^', include('hustle_science_pkg.urls'))
)
