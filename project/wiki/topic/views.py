from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from tools import logging_check
from tools.logging_check import *
from .models import *
# Create your views here.
from message.models import *


@logging_check('DELETE','POST')
def topic(request,username=None):
    if request.method == 'GET':
        #获取  用户文章数据
        #/v1/topics/guoxiaonao  - guoxiaonao的所有文章
        #/v1/topics/guoxiaonao?category=tec/no-tec  查看具体种类
        #/v1/topics/guoxiaonao?t_id=33  查看具体文章

        # username = request.username
        category = request.GET.get('category')
        t_id = request.GET.get('t_id')
        author = Userprofile.objects.get(username=username)
        if not author:
            result = {'code': 30104, 'error': 'The author is not existed !'}
            return JsonResponse(result)
        visitor = get_user_by_request(request)
        visitor_username = None
        print(visitor)
        if visitor:
            visitor_username = visitor.username
        if t_id:
            is_self = False
            t_id = int(t_id)
            #获取指定文章的详情页
            if username == visitor_username:
                try:
                    author_topic = Topic.objects.get(id=t_id)
                    is_self = True
                except Exception as e:
                    print('--get t_id error--')
                    print(e)
                    result = {'code':30108,'error':'No topic'}
                    return JsonResponse(result)
            else:
                try:
                    author_topic = Topic.objects.get(id=t_id,limit='public')
                except Exception as e:
                    print('--get t_id error--')
                    print(e)
                    result = {'code': 30109, 'error': 'No topic visitor'}
                    return JsonResponse(result)

            res = make_topic_res(author,author_topic,is_self)
            return JsonResponse(res)


        elif category in ['tec','no-tec'] :
            user1 = Topic.objects.filter(author_id=username,category = category)
            l1 = []
            dic = {'code': 200}
            for user in user1:
                a = {'id': user.id, 'title': user.title, 'category': user.category,
                     'created_time': user.create_time,
                     'introduce': user.introduce,
                     'author': user.author_id
                     }
                l1.append(a)
            dic['data'] = {'nickname': author.nickname, 'topics': l1}
            return JsonResponse(dic)
        else:
            #是博主
            if username == visitor_username:
                author_topic = Topic.objects.filter(author_id=username)
            else:
                author_topic = Topic.objects.filter(author_id=username,limit = 'public')

            l1 = []
            dic = {'code': 200}
            for user in author_topic:
                a = {'id': user.id, 'title': user.title, 'category': user.category,
                     'created_time': user.create_time,
                     'introduce': user.introduce,
                     'author': user.author_id
                     }
                l1.append(a)
            dic['data'] = {'nickname': author.nickname, 'topics': l1}
            return JsonResponse(dic)
    elif request.method == 'DELETE':
        id = request.GET.get('topic_id')
        try:
            topic1 = Topic.objects.get(id=id)
            topic1.delete()
            return JsonResponse({'code':200})
        except:
            return JsonResponse({'code':30101})
    elif request.method == 'POST':
        # print(request)
        author = request.user
        print('=======',author.username)
        # print(username)
        # if author.username != username:
        #     dic = {'code':30101,'error':'The author is error'}
        #     return JsonResponse(dic)
        data = request.body
        data = json.loads(data)
        #b'{"content":"<p>fff<br></p>","content_text":"fff","limit"
        # :"public","title":"ddd","category":"tec"}'
        # print(data)
        content = data.get('content')
        content_text =data.get('content_text')
        limit = data.get('limit')
        title = data.get('title')
        import html
        title = html.escape(title) #将标题转化为非代码格式  防止攻击
        category = data.get('category')
        if category not in['tec','no-tec']:
            res = {'code':30102,'error':'Thanks,you category is wrong'}
            return JsonResponse(res)
        Topic.objects.create(title=title,category=category,limit=limit,content=content,author_id=username,introduce =
        content_text[:15])
        return JsonResponse({'code':200,'username':username})

def make_topic_res(author, author_topic,is_self):
    #获取上一篇文章的id和title
    #获取下一篇文章的id和title
    if is_self:
        #博主自己访问自己的博客
        next_topic = Topic.objects.filter(id__gt=author_topic.id,author_id=author).first()
        last_topic = Topic.objects.filter(id__lt=author_topic.id,author_id=author).last()
    else:
        #访客访问他人的博客
        next_topic = Topic.objects.filter(id__gt=author_topic.id, author_id=author,limit ='public').first()
        last_topic = Topic.objects.filter(id__lt=author_topic.id, author_id=author,limit='public').last()
    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    else:
        next_id = None
        next_title = None
    if last_topic:
        last_id = last_topic.id
        last_title = last_topic.title
    else:
        last_id = None
        last_title = None
    res = {'code':200,'data':{}}
    res['data']['title'] = author_topic.title
    res['data']['nickname'] = author.nickname
    res['data']['content'] = author_topic.content
    res['data']['introduce'] = author_topic.introduce
    res['data']['created_time']  = author_topic.create_time.strftime('%Y-%m-%d %H:%M:%S')
    res['data']['author'] = author.nickname
    res['data']['next_id'] = next_id
    res['data']['next_title'] = next_title
    res['data']['last_title'] = last_title
    res['data']['last_id'] = last_id
    #留言
    #TODO 添加留言显示
    #获取当前文章的所有留言
    print(author_topic)
    all_messages = Message.objects.filter(topic_id=author_topic).order_by('-created_time')
    m_count = 0
    # 留言专属容器
    msg_list = []
    # 回复专属容器
    reply_home = {}
    for message in all_messages:
        m_count += 1
        if message.parent_message:
            # 回复
            reply_home.setdefault(message.parent_message, [])
            reply_home[message.parent_message].append(
                {'msg_id': message.id, 'content': message.content, 'publisher': message.publisher_id.nickname,
                 'publisher_avatar': str(message.publisher_id.avatar),
                 'created_time': message.created_time.strftime('%Y-%m-%d %H:%M:%S')})

        else:
            # 留言
            msg_list.append({'id': message.id, 'content': message.content, 'publisher': message.publisher_id.nickname,
                             'publisher_avatar': str(message.publisher_id.avatar),
                             'created_time': message.created_time.strftime('%Y-%m-%d %H:%M:%S'), 'reply': []})

    # 关联 留言及回复
    for m in msg_list:
        if m['id'] in reply_home:
            m['reply'] = reply_home[m['id']]

    res['data']['messages'] = msg_list
    res['data']['messages_count'] = m_count

    # print('显示data')
    # print('data',data)
    # handle_data = handle_message(data)
    # print('handle_data',handle_data)
    # res['data']['messages'] = []
    # res['data']['messages_count'] = 0
    return res

def handle_message(data):
    print('data++++',data)
    l2 = []
    for i in range(len(data)):
        dic = {}
        l11 = []
        for j in range(i + 1, len(data)):
            if data[i].id == data[j].parent_message:
                dic['id'] = data[i].id
                l11.append({'id': data[j].id})
        else:
            if not dic:
                continue
            dic['children'] = l11
            l2.append(dic)
    return l2