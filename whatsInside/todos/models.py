# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from whatsInside.settings  import AUTH_USER_MODEL

class Todo(models.Model): 
    description = models.CharField(max_length=1000) 
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    isComplete = models.BooleanField(default=False)
    currentDate = models.DateField(auto_now=True)
    finishBy = models.DateField()
