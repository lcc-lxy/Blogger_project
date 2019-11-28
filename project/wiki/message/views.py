import json

import jwt

from tools import logging_check
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import html
from message.models import *
# Create your views here.
@logging_check.logging_check('POST')
def message(request,topic_id=None):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)
        content = data.get('content')
        parent_id = data.get('parent_id',0)
        #TODO 参数检测
        #检测topic是否存在
        try:
            topic = Topic.objects.get(id=topic_id)
        except Exception as e:
            result = {'code':40101,'error':'No topic'}
            return JsonResponse(result)
        token = request.META.get('HTTP_AUTHORIZATION')
        res = jwt.decode(token,'123456','HS256')
        username = res['username']
        user = Userprofile.objects.get(username=username)
        Message.objects.create(content=content,parent_message = parent_id,publisher_id=user,topic_id=topic)
        # print(parent_id)
        # content = html.escape(content)
        # print(content)
        # if not content:
        #     res = {'code': 15012, 'error': 'u no content'}
        #     return JsonResponse(res)
        res = {'code':200,'data':content}

        return JsonResponse(res)
    if request.method=='GET':
        all_m = Message.objects.all()
        all_list= []
        for  i in all_m:
            d ={}
            d['id'] = i.id
            d['content'] = i.content
            d['parent_message'] = i.parent_message
            d['publisher'] = i.publisher_id.username
            d['topic'] = i.topic_id.id
            all_list.append(d)
        return JsonResponse({'code':200,'data':all_list})