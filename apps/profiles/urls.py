from django.conf.urls.defaults import *

urlpatterns = patterns('profiles.views',

    url(r'^(?P<username>[\.\w]+)/comments/$',
        'profile_comments',
        name='profile_comments'),

    url(r'^(?P<username>[\.\w]+)/fan/$',
        'become_profile_fan',
        name='profile_become_fan'),

    url(r'^(?P<username>[\.\w]+)/unfan/$',
        'stop_being_profile_fan',
        name='profile_stop_being_fan'),

)

