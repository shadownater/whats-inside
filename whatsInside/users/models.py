# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser

from django.db import models
import uuid

class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.email
