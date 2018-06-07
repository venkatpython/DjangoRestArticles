# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(_('Article name'), max_length=64)
    content = models.TextField(_('Article content'), blank=True, null=True)
    author = models.CharField(_('Author name'), max_length=64)
    votes = models.IntegerField(_('Votes'), default=0)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
