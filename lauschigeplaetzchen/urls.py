from django.conf.urls import patterns, include, url
from django.conf import settings

import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lauschigeplaetzchen.views.home', name='home'),
    # url(r'^lauschigeplaetzchen/', include('lauschigeplaetzchen.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^orte/(?P<slug>[-\w]+)/$', 'places.views.detail'),
    (r'^$', 'places.views.index'),
    (r'^submit/', 'places.views.submit'),
    (r'^about/', 'places.views.about'),
    (r"^orte/add_comment/(?P<slug>[-\w]+)/$", "places.views.add_comment"),
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(.*)$', 'django.views.static.serve', kwargs={'document_root': os.path.join(SITE_ROOT, 'media')}), )

