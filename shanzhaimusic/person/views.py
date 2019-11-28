from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import render
import json

from users.models import User
from .models import *
# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'person/one.html')
    if request.method=='POST':
        if not request.session.get('username'):
            if not request.COOKIES.get('username'):
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = request.COOKIES['username']

        username = request.session.get('username')
        user = User.objects.get(username=username)

        data = request.POST.get('data')

        user.info = data
        user.save()
        # print(data)
        return JsonResponse({'code':200,'data':data})
def diary(request):
    if request.method =='GET':
        return render(request,'person/diary.html')
    if request.method=='POST':
        if not request.session.get('username'):
            if not request.COOKIES.get('username'):
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = request.COOKIES['username']

        username = request.session.get('username')
        user = User.objects.get(username=username)
        user_id = user.id

        data = request.POST.get('data')
        if not data:
            return JsonResponse({'code': 203, 'data': '请输入内容'})
        # user_id = 10
        # print(data)
        Person_diary.objects.create(user_id=user,content=data)
        return JsonResponse({'code':200,'data':'成功'})
def handle_index(request):
    if request.method=='POST':
        if not request.session.get('username'):
            if not request.COOKIES.get('username'):
                return HttpResponseRedirect('/user/login')
            else :
                request.session['username'] = request.COOKIES['username']

        username = request.session.get('username')
        user = User.objects.get(username=username)
        user_id = user.id

        print(user_id)
        data = Person_diary.objects.filter(user_id=user)
        l1 =[]
        for d in data:
            dic={}
            dic['created_time']=d.created_time
            dic['content'] = d.content
            l1.append(dic)
        photo = Person_photo.objects.filter(user_id=user_id)
        l2= []
        for d in photo:
            dic1={}
           # dic['created_time']=d.created_time
            dic1['avator'] = str(d.avatar)
            l2.append(dic1)
        print(l2)
        info = 'success'
        # print(l1)
        return JsonResponse({'code':200,'diary':l1,'info':info,'photo':l2})
def photo(request):
    if request.method=='GET':
        return render(request,'person/update_photo.html')
        # return HttpResponse('dd')
def handle_photo(request):
    if request.method=='GET':
        return JsonResponse({'code':200})
    if request.method =='POST':
        photo =  request.FILES['avatar']
        # user_id = 10
        if not request.session.get('username'):
            if not request.COOKIES.get('username'):
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = request.COOKIES['username']

        username = request.session.get('username')
        user = User.objects.get(username=username)
        user_id = user.id

        Person_photo.objects.create(user_id=user,avatar=photo)
        return JsonResponse({'code':200})


def username(request):
    if not request.session.get('username'):
        if not request.COOKIES.get('username'):
            return HttpResponseRedirect('/user/login')
        else:
            request.session['username'] = request.COOKIES['username']

    username = request.session.get('username')
    return JsonResponse({'code':200,'data':{'username':username}})

def info(request):
    if not request.session.get('username'):
        if not request.COOKIES.get('username'):
            return HttpResponseRedirect('/user/login')
        else:
            request.session['username'] = request.COOKIES['username']

    username = request.session.get('username')
    user = User.objects.get(username=username)
    print(user.info)
    return JsonResponse({'code':200,'data':{'info':user.info}})


