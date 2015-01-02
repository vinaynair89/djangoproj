from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'collection.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^about/', 'collection.views.about', name='about'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^contact-me/$', 'collection.views.contact', name='contact'),
    url(r'^admin/$', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
