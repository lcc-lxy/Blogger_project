import sys

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


# Create your views here.
def base(request):
    # 带分页的book列表页
    all_musician = Musician.objects.all()
    # 分页器 初始化paginator对象  (列表,每页显示条数)
    paginator = Paginator(all_musician, 9)
    # 127.0.0.1:8000/index/book?page=1  获取  第1页  为page对象
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    print('=======================================')
    print(all_musician)
    print(page)
    print(request.path)
    print('=======================================')
    return render(request, 'musician/base.html')


def musician(request):
    # 带分页的book列表页
    all_musician = Musician.objects.all()
    # all_musician = Musician.objects.all()
    # 分页器 初始化paginator对象  (列表,每页显示条数)
    paginator = Paginator(all_musician, 9)
    # 127.0.0.1:8000/index/book?page=1  获取  第1页  为page对象
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    filename = 'musician'

    return render(request, 'musician/musician.html', locals())


def musician_lx(request):
    # 带分页的book列表页
    all_musician = Musician.objects.filter(style=1)
    # 分页器 初始化paginator对象  (列表,每页显示条数)
    paginator = Paginator(all_musician, 9)
    # 127.0.0.1:8000/index/book?page=1  获取  第1页  为page对象
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    filename = 'musician_lx'

    return render(request, 'musician/musician_lx.html', locals())


def musician_yg(request):
    # 带分页的book列表页
    all_musician = Musician.objects.filter(style=2)
    # 分页器 初始化paginator对象  (列表,每页显示条数)
    paginator = Paginator(all_musician, 9)
    # 127.0.0.1:8000/index/book?page=1  获取  第1页  为page对象
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    filename = 'musician_yg'

    return render(request, 'musician/musician_yg.html', locals())


def musician_dz(request):
    # 带分页的book列表页
    all_musician = Musician.objects.filter(style=3)
    # 分页器 初始化paginator对象  (列表,每页显示条数)
    paginator = Paginator(all_musician, 9)
    # 127.0.0.1:8000/index/book?page=1  获取  第1页  为page对象
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    filename = 'musician_dz'

    return render(request, 'musician/musician_dz.html', locals())


def musician_my(request):
    # 带分页的book列表页
    all_musician = Musician.objects.filter(style=4)
    # 分页器 初始化paginator对象  (列表,每页显示条数)
    paginator = Paginator(all_musician, 9)
    # 127.0.0.1:8000/index/book?page=1  获取  第1页  为page对象
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    filename = 'musician_my'

    return render(request, 'musician/musician_my.html', locals())


def musician_js(request):
    # 带分页的book列表页
    all_musician = Musician.objects.filter(style=5)
    # 分页器 初始化paginator对象  (列表,每页显示条数)
    paginator = Paginator(all_musician, 9)
    # 127.0.0.1:8000/index/book?page=1  获取  第1页  为page对象
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    filename = 'musician_js'

    return render(request, 'musician/musician_js.html', locals())
