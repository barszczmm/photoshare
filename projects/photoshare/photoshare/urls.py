from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photoshare.views.home', name='home'),
    # url(r'^photoshare/', include('photoshare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('userena.urls')),

    url(r'^accounts/', include('profiles.urls')),

    url(r'^messages/', include('userena.contrib.umessages.urls')),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^', include('photos.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
