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
    birthday = models.DateField(_("birthday"), blank=True, null=True)
    about_me = models.TextField(_("about me"), blank=True, null=True)
    website = models.URLField(_("website"), blank=True, null=True)
    fan_of = models.ManyToManyField('self', symmetrical=False, related_name='fans')

    @models.permalink
    def get_absolute_url(self):
        return ('userena_profile_detail', (), {'username': self.user.username})
    get_absolute_url.short_description = 'url'


