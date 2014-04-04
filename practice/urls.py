from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
)
