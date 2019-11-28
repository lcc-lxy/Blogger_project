from django.http import *
from django.shortcuts import render

from users.models import User


def index(request):
    if request.method == 'GET':
        return render(request,'index.html')


def exit(request):
    try:
        uname = request.session.get('username')

    except Exception as e:
        print('request.session.get("username")报错',e)
        return render(request,'index.html')

    if uname :
        del request.session['username']
        resp = HttpResponseRedirect('/index')
        resp.delete_cookie('username')
        return resp
    else:
        return HttpResponseRedirect('/index')


def index_server(request):

    if not request.session.get('username'):
        if not request.COOKIES.get('username'):
            return JsonResponse({})
        else:
            request.session['username'] = request.COOKIES['username']

    uname = request.session.get('username')
    if uname:

        return JsonResponse({'username':uname})
    else :
        return JsonResponse({})

def message(request):
    page = request.GET.get('page')
    if page == '1':
        return render(request,'message01.html')
    if page == '2':
        return render(request,'message02.html')
    if page == '3':
        return render(request,'message03.html')
    if page == '4':
        return render(request,'message04.html')




