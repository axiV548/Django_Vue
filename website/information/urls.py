# -*- coding: utf-8 -*-
# author：albert time:2020/4/28

from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_information)
]