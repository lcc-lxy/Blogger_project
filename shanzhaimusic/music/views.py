from django.http import *
from django.shortcuts import render

# Create your views here.
from discuss.models import Discuss
from music.models import Music
from users.models import User


def search(request):
    if request.method == 'GET':
        man = request.GET.get('man')
        if man :
            music_names = Music.objects.filter(music_name__contains=man)

            singer_names = Music.objects.filter(singer__contains=man)

            if music_names or singer_names:
                return render(request, 'music/search.html', locals())
        else :
            music_names = Music.objects.all()

            return render(request, 'music/search.html', locals())


    elif request.method == 'POST':

        name = request.POST.get('search')

        music_names = Music.objects.filter(music_name__contains=name)

        singer_names = Music.objects.filter(singer__contains=name)

        if music_names or singer_names :

            return render(request,'music/search.html',locals())

        else :
            dict1 = {'x':'nofind'}
            dict1['name'] = name
            return render(request,'music/search.html',dict1)


def player(request,music_id):
    if request.method == 'GET':
        try :
            music = Music.objects.get(id=music_id)
        except Exception:
            return HttpResponseRedirect('/index')
        if music :
            return render(request,'music/player.html',locals())


def discuss(request):
    if request.method == 'GET':

        music_id = request.GET.get('music_id')
        music = Music.objects.get(id=music_id)
        all_dis = Discuss.objects.filter(music_id_id=music_id).order_by('-created_time')
        all_dis1 = Discuss.objects.filter(music_id_id=music_id,parent_id=0)
        all_list = []
        print(all_dis)
        reply = {}
        for dis in all_dis:
            user = User.objects.get(id=dis.user_id_id)

            if dis.parent_id == 0:

                dict1 = {'discuss':dis.message,'music_name':music.music_name,'id':dis.id,
                         'username':user.username,'created_time':dis.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                         'reply':[],'music_id':music_id}
                all_list.append(dict1)

            else :

                reply.setdefault(dis.parent_id,[])
                dict2 = {'discuss': dis.message, 'music_name': music.music_name, 'id': dis.id,'username':user.username,'created_time':dis.created_time.strftime('%Y-%m-%d %H:%M:%S')}
                reply[dis.parent_id].append(dict2)


        for m in all_list:
            if m['id'] in reply:
                m['reply'] = reply[m['id']]

        return  JsonResponse({'code':200,'discuss_count':len(all_dis1),'data':all_list})

    elif request.method == 'POST':
        if not request.session.get('username'):
            if not request.COOKIES.get('username'):
                return HttpResponseRedirect('/user/login')
            else :
                request.session['username'] = request.COOKIES['username']

        music_id = request.GET.get('music_id')
        message = request.POST.get('message')
        print('----------',music_id,'--',message)

        if message:
            username = request.session.get('username')
            user = User.objects.get(username=username)
            music = Music.objects.get(id=music_id)

            discuss = Discuss(message=message, user_id=user, music_id=music, parent_id=0)

            discuss.save()
            return JsonResponse({'code':200})


        music_id = request.GET.get('music_id')
        discuss_id = request.GET.get('discuss_id')
        d_message = request.POST.get('discuss')
        # print(music_id,discuss_id,d_message)

        username = request.session.get('username')
        user = User.objects.get(username=username)
        music = Music.objects.get(id=music_id)

        if d_message:
            dis = Discuss(message=d_message,user_id=user,music_id=music,parent_id=discuss_id)
            dis.save()

        else :
            dis = Discuss(message=d_message, user_id=user, music_id=music, parent_id=0)
            dis.save()

        return JsonResponse({'code': 200})

def up(request,music_id):

    m_id = int(music_id) - 1
    if m_id <= 0:
        m_id = 10

    return HttpResponseRedirect('/music/player/%s'%m_id)

def down(request,music_id):

    m_id = int(music_id) + 1
    if m_id >= 10:
        m_id = 1

    return HttpResponseRedirect('/music/player/%s'%m_id)


