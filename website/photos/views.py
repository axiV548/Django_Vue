from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import 艺人
from .models import 个人图片
# Create your views here.

from django.http import JsonResponse
from django.core import serializers
import json

def show_photos(request):
    if request.method == "GET":
        page = request.GET.get('page')
        if request.GET.get('name'):     #如果传入带名字参数则返回个人图片
            name = request.GET.get('name')
            艺人名 = 艺人.objects.filter(名字=name)
            图片集 = 个人图片.objects.filter(名字=name)
            if not 艺人名:
                return JsonResponse({'status': 0, 'data': 'bad request'})
        else:
            艺人名 = 艺人.objects.all()
            图片集 = 个人图片.objects.all()    #从数据库获取数据QuerySet类型
        paginator = Paginator(图片集, 10)   #分页（数据， 每页几个， 少于等于几个不另外分页）
        try:
            now_photo = paginator.page(page)
        except PageNotAnInteger:
            now_photo = paginator.page(1)
        except EmptyPage:
            now_photo = paginator.page(paginator.num_pages)
        艺人名 = json.loads(serializers.serialize("json", 艺人名))  #QuerySet类型转json
        # 图片集 = json.loads(serializers.serialize("json", 图片集))
        now_photo = json.loads(serializers.serialize("json", now_photo))
        # print(now_tupian)
        data = {'status': 1, 'data': 艺人名, 'image': now_photo, 'page': page}
        # print(data)
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 0, 'data': 'bad request'})

def upload(request):
    if request.method == "GET":
        return JsonResponse({'status': 0, 'data': 'bad request'})
    elif request.method == "POST":      #接收POST上传请求
        for ph in request.FILES.getlist('photo'):
            photos = 个人图片()
            name = request.POST['name']     #根据提取的名字分类
            photos.名字 = name
            photos.关联 = 艺人.objects.get(名字=name)     #添加关联
            photos.图片 = ph
            photos.save()
        return JsonResponse({'status': 1, 'data': 'Uploaded successfully'})

