from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', views.TodoView)

urlpatterns = [
    path('', include(router.urls))
    ]
