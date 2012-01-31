from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from djangoratings.views import AddRatingFromModel

from views import PhotosListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, rate_photo

urlpatterns = patterns('',

    url(r'^photos/$',
        PhotosListView.as_view(),
        name='photos_list_photos'),

    url(r'^users/(?P<username>[\.\w]+)/photos/$',
        PhotosListView.as_view(),
        name='profile_photos'),

    url(r'^photos/(?P<photo_id>[\d]+)/$',
        PhotoDetailView.as_view(),
        name='photos_show_photo'),

    url(r'^photos/add/$',
        PhotoCreateView.as_view(),
        name='photos_add_photo'),

    url(r'^photos/(?P<photo_id>[\d]+)/edit/$',
        PhotoUpdateView.as_view(),
        name='photos_edit_photo'),

    url(r'^photos/(?P<photo_id>[\d]+)/delete/$',
        PhotoDeleteView.as_view(),
        name='photos_remove_photo'),

    url(r'^photos/(?P<photo_id>[\d]+)/comments/$',
        PhotoDetailView.as_view(template_name='photos/photo_comments.html'),
        name='photos_comments_photo'),

    url(r'^photos/(?P<photo_id>[\d]+)/ratings/$',
        PhotoDetailView.as_view(template_name='photos/photo_ratings.html'),
        name='photos_ratings_photo'),

    url(r'photos/(?P<photo_id>\d+)/rate/(?P<score>\d+)/',
        rate_photo,
        name='photos_rate_photo'),

)
