import time
def f1(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2 = time.time()
        print(t2-t1)
        # return func(*args,**kwargs)
    return wrapper
@f1
def f2():
    print('哈哈哈')
# print(f2())
l1 = [{'id':1,'parent_id':0},{'id':2,'parent_id':1},{'id':3,'parent_id':1},{'id':4,'parent_id':0},{'id':5,
                                                                                      'parent_id':4}]
# @f1
def f3(l1):
    l2 = []
    for i in range(len(l1)):
        dic = {}
        l11 = []
        for j in range(i+1,len(l1)):
            if l1[i]['id'] == l1[j]['parent_id']:
                dic['id'] = l1[i]['id']
                l11.append({'id':l1[j]['id']})
        else:
            if not dic:
                continue
            dic['children'] = l11
            l2.append(dic)
    return l2
a = f3(l1)
print(a)
# print(l2)
# def f3(array1):
#     dic={}
#     for i in array1:
#         if i['parent_id'] ==0:
#             list.append(i)
#         else:
#             p_id = i['parent_id']
#             if p_id not in dic:
#                 dic[p_id] =[]
#                 # dic[p_id].append({'id':})


