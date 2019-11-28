from django.http import JsonResponse
from user.models import Userprofile
import redis
def test(request):
    r = redis.Redis(host='127.0.0.1',port=6379,db=0)
    while True:
        try:
            with r.lock('lcc',blocking_timeout=3) as lock:
                print(lock)
                u = Userprofile.objects.get(username = 'lcc')
                u.score += 1
                u.save()
            break
        except Exception as e:
            print('Lock failed')
    return JsonResponse({'code':200,'data':{}})
