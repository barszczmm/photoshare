# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from djangoratings.fields import RatingField


def get_upload_path(instance, filename):
    return 'users/%s/%s' % (instance.user.username, filename)

class Photo(models.Model):
    """
    Photo uploaded by user.
    """
    user = models.ForeignKey(User, related_name='photos')
    image = models.ImageField(_("image"), upload_to=get_upload_path)
    title = models.CharField(_("title"), max_length=200)
    description = models.TextField(_("description"), blank=True, null=True)
    uploaded_at = models.DateTimeField(_("uploaded at"), auto_now_add=True)
    rating = RatingField(range=5)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photos_show_photo', (), {'photo_id': self.id})
    get_absolute_url.short_description = 'url'

    class Meta:
        get_latest_by = 'uploaded_at'
        ordering = ['-uploaded_at']
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')


