# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


def get_upload_path(instance, filename):
    return 'users/%s/%s' % (instance.user.username, filename)

class Photo(models.Model):
    """
    Photo uploaded by user.
    """
    user = models.ForeignKey(User)
    title = models.CharField(_("title"), max_length=200)
    image = models.ImageField(_("image"), upload_to=get_upload_path)
    description = models.TextField(_("description"), blank=True)
    uploaded = models.DateTimeField(_("uploaded"), auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        return ('photos_show_photo', (), {'photo_id': self.id})
    get_absolute_url.short_description = 'url'

    class Meta:
        get_latest_by = 'uploaded'
        ordering = ['-uploaded']


