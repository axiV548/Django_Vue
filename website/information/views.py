from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.core import serializers
import json

from .models import information

def show_information(request):
    if request.method == "GET":
        内容 = information.objects.all()  #从数据库获取数据QuerySet类型
        内容 = json.loads(serializers.serialize("json", 内容))  #QuerySet类型转json
        data = {'status': 1, 'data': 内容}
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 0, 'data': 'bad request'})
