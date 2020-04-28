from django.shortcuts import render

from .models import 艺人
from .models import 个人图片
# Create your views here.

from django.http import JsonResponse
from django.core import serializers
import json

def show_photos(request):
    艺人名 = 艺人.objects.all()
    图片集 = 个人图片.objects.all()

