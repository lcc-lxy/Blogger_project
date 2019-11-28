import datetime
import json
import hashlib
import time
import re
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from user.weiboapi import OAuthWeibo
from .models import *
import jwt
from tools import logging_check
from wtoken.views import make_token
# Create your views here.
@logging_check.logging_check('PUT')
def users(request,username=None):
    print('hello')
    if request.method == 'GET':
        #拿数据
        if not username:
            users_data = []
            all_user = Userprofile.objects.all()
            for user in all_user:
                dic = {}
                dic['nicknae'] = user.nickname
                dic['username'] = user.username
                dic['sign'] = user.sign
                dic['info'] = user.info
                users_data.append(dic)
            return JsonResponse({'code':200,'data':users_data})
        if username:
            user = Userprofile.objects.filter(username=username)
            if not request.GET.keys():
                dic = {}
                for user in user:
                    dic['nickname'] = user.nickname
                    dic['username'] = user.username
                    dic['sign'] = user.sign
                    dic['info'] = user.info
                    dic['avatar'] = str(user.avatar)
                return JsonResponse({'code':200,'data':dic})
            elif request.GET.keys():
                dic = {}
                for user1 in request.GET.keys():
                    if user1 =='password':
                        continue   #过滤密码
                    if hasattr(user[0],user1):
                        dic[user1] = getattr(user[0],user1)
                return JsonResponse({'code': 200, 'data':dic})

    elif request.method =='POST':
        #创建用户
        json_str = request.body
        json_obj = json.loads(json_str)
        print(json_obj)
        username = json_obj['username']
        pwd1 = json_obj['password_1']
        pwd2 = json_obj['password_2']
        email = json_obj['email']
        if not username:
            return JsonResponse({'code':10101,'error':'Please give me a username'})
        elif not email :
            return JsonResponse({'code': 10104, 'error': 'You not input a email'})
        elif not re.findall(r'\S+@\S+\.com',email):
            return JsonResponse({'code': 10104, 'error': 'You not input a type of email'})
        elif not pwd1:
            return JsonResponse({'code': 10102, 'error': 'Please input  a password'})
        elif pwd1!=pwd2:
            return JsonResponse({'code': 10103, 'error': 'You input password is difference in two times'})
        else:
            pwd1 = hashlib.md5(pwd1.encode())
            pwd1 = pwd1.hexdigest()
            # token = {'username':username,'exp':300+time.time()}
            token = make_token(username,300,datetime.datetime.now())
            # token = jwt.encode(token,'123456',algorithm='HS256')
            Userprofile.objects.create(username=username,password=pwd1,email=email)
            print('token:',token)
            return JsonResponse({'code':200,'username':username,'data':{'token':token.decode()}})

    elif request.method =='PUT':
        #更新
        if not username:
            res = {'code':10108,'error':'Must be give me a username'}
            return JsonResponse(res)
        if username:
            json_str = request.body
            json_str = json.loads(json_str)
            nickname = json_str.get('nickname')
            sign = json_str.get('sign')
            info = json_str.get('info')
            # user = Userprofile.objects.filter(username=username)[0]
            user = request.user
            print('request user',user)
            if user.username != username:
                res = {'code':10109,'error':'username is error'}
                return JsonResponse(res)
            print(user)
            print('/'*50)
            print('nickname:'+nickname)
            print('sign:'+sign)
            print('/'*50)
            to_update = False
            if nickname != user.nickname:
                to_update = True
            if sign != user.sign:
                to_update = True
            if info != user.info:
                to_update = True
            print(to_update)
            if to_update:
                user.nickname = nickname
                user.sign = sign
                user.info = info
                user.save()
                print(user.nickname,user.info)
                print('成功')
            return JsonResponse({'code':200,'username':username})

@logging_check.logging_check('POST')
def users_avatar(request,username):
    #处理头像上传
    if request.method !='POST':
        result = {'code':10110,'error':'Please use POST'}
        return JsonResponse(result)
    user = request.user
    if user.username != username:
        result = {'code':10109,'error':'The username is error'}
        return JsonResponse(result)

    user.avatar = request.FILES['avatar']
    user.save()
    return JsonResponse({'code':200,'username':username})

def users_weibo_url(request):
    oauth = OAuthWeibo('123')
    oauth_weibo_url = oauth.get_weibo_login()
    return JsonResponse({'code':200,'oauth_url':oauth_weibo_url})

# def make_token(username,exp):
#     key = '123456'
#     now_t = time.time()
#     payload = {
#         'username':username,'exp':int(exp+now_t)
#     }
#     return jwt.encode(payload,key,algorithm='HS256')