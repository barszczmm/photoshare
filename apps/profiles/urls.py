from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',

    url(r'^(?P<username>[\.\w]+)/comments/$',
        'profile_comments',
        name='profile_comments'),

)