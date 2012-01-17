# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from userena.models import UserenaBaseProfile


class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
    gender = models.CharField(_("gender"), max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.PositiveSmallIntegerField(_("age"), blank=True, null=True)
    about = models.TextField(_("about"), blank=True)
    website = models.URLField(_("website"), blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('userena_profile_detail', (), {'username': self.user.username})
    get_absolute_url.short_description = 'url'

