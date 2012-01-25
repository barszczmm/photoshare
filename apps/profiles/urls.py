from django.conf.urls.defaults import *
#from django.contrib.auth import views as auth_views

#from userena import views as userena_views

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

    # AJAX vesrions of some userena views
    #url(r'^signup/ajax/$',
       #userena_views.signup,
       #{'template_name': 'userena/signup_form_ajax.html'},
       #name='userena_signup_ajax'),
    #url(r'^signin/ajax/$',
       #userena_views.signin,
       #{'template_name': 'userena/signin_form_ajax.html'},
       #name='userena_signin_ajax'),
    #url(r'^password/reset/ajax/$',
       #auth_views.password_reset,
       #{'template_name': 'userena/password_reset_form_ajax.html',
        #'email_template_name': 'userena/emails/password_reset_message.txt'},
       #name='userena_password_reset_ajax'),
)

