import json
import time
import hashlib
import jwt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from user.models import *
import datetime
# Create your views here.
def tokens(request):
    if request.method !='POST':
        result = {'code':20101,'error':'Please use Post'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj['username']
    pwd = json_obj['password']
    user = Userprofile.objects.filter(username=username)
    if not user:
        result = {'code':20102,'error':'The username or password is error'}
        return JsonResponse(result)
    pwd = hashlib.md5(pwd.encode())
    pwd = pwd.hexdigest()
    if pwd != user[0].password:
        result = {'code': 20103, 'error': 'The username or password is error'}
        return JsonResponse(result)
    now_datatime = datetime.datetime.now()
    user[0].login_time = now_datatime
    user[0].save()
    #生成token
    token = make_token(username,60*60*24,now_datatime)
    result = {'code':200,'username':username,'data':{'token':token.decode()}}
    return JsonResponse(result)
def make_token(username,exp,now_datatime):
    key = '123456'
    now_t = time.time()
    print('now_t',now_t)
    # login_time =
    payload = {
        'username':username,'exp':int(exp+now_t),'login_time':str(now_datatime)
    }
    return jwt.encode(payload,key,algorithm='HS256')