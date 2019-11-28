import jwt
from django.http import JsonResponse
from user.models import Userprofile

TOKEN_KEY = '123456'
def logging_check(*methods):
    def _login_check(func):
        def wrapper(request,*args,**kwargs):
            #逻辑判断
            #1.判断当前请求是否需要校验
            if not methods:
                return func(request,*args,**kwargs)
            else:
                # print(request.method)
                # print(methods)
                if request.method not in methods:
                    return func(request,*args,**kwargs)
            #2.取出token
            print('logging_check中的requset_method',request.method)
            print('123')
            token = request.META.get('HTTP_AUTHORIZATION')
            if not token:
                res = {'code':20104,'error':'Please login'}
                return JsonResponse(res)
            #3.如果需要校验token,如何校验
            try:
                res = jwt.decode(token,TOKEN_KEY,'HS256')
                # print('这是logging_check 的res',res)
            except Exception as e:
                res = {'code': 20105, 'error': 'Please login'}
                return JsonResponse(res)
            username = res['username']
            #取出token里的login_time
            login_time = res.get('login_time')
            user = Userprofile.objects.get(username=username)
            if login_time:
                if str(user.login_time) != login_time:
                    res = {'code':20106,'error':'Other people have logined! Please login again!'}
                    return JsonResponse(res)
            request.user = user
            return func(request,*args,**kwargs)
        return wrapper
    return _login_check

def get_user_by_request(request):
    #尝试获取用户身份
    #return user or None
    token = request.META.get('HTTP_AUTHORIZATION')
    print('token',token)
    if not token:
        #用户没登录
        return None
    try:
        res = jwt.decode(token, TOKEN_KEY, algorithms='HS256')
    except Exception as e:
        return None
    print('res',res)
    username = res['username']
    users = Userprofile.objects.filter(username=username)
    print(users)
    if not users:
        return None
    return users[0]