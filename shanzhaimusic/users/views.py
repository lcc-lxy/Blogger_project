from django.shortcuts import render

# Create your views here.
from users.models import User


def login(request):
    if request.method == 'GET':
        if not request.session.get('username'):
            if not request.COOKIES.get('username'):
                return render(request,'users/login.html')
            else :
                request.session['username'] = request.COOKIES['username']

        return render(request,'/users/index.html')

    elif request.method == 'POST':

        try :
            zname = request.POST.get('name')
            zpw = request.POST.get('password')
            zpw1 = request.POST.get('password1')
            lname = request.POST.get('lname')
            lpw = request.POST.get('lpassword')
        except Exception:

            return render(request,'users/login.html')

        if zname and zpw and zpw1 :
            if zpw == zpw1 :
                try :
                    user = User(username=zname,password=zpw)
                    user.save()
                except Exception:
                    dict1 = {'x':'unknown'}
                    return render(request,'users/login.html',dict1)
                dict1 = {'x':'zyes'}
                return render(request,'users/login.html',dict1)
            else :
                dict1 = {'x':'pw!=pw1'}
                return render(request, 'users/login.html', dict1)
        elif not zname and not lname:
            dict1 = {'x': 'nonename'}
            return render(request, 'users/login.html', dict1)
        elif not zpw and not lname:
            dict1 = {'x':'nonepw'}
            return render(request, 'users/login.html', dict1)
        elif not zpw and not lname:
            dict1 = {'x': 'nonepw1'}
            return render(request, 'users/login.html', dict1)

        if lname and lpw:
            try:
                user1 = User.objects.get(username=lname)
            except Exception:
                dict1 = {'x': 'nolname'}
                return render(request, 'users/login.html', dict1)

            if lpw == user1.password :

                request.session['username'] = lname
                dict1 = {'x': 'lyes'}
                resp = render(request, 'users/login.html', dict1)
                resp.set_cookie('username',lname,max_age=60*60*24)
                return resp
            else :
                dict1 = {'x': 'lno'}
                return render(request, 'users/login.html', dict1)
        elif not lname:
            dict1 = {'x': 'notlname'}
            return render(request, 'users/login.html', dict1)
        elif not lpw:
            dict1 = {'x': 'notlpw'}
            return render(request, 'users/login.html', dict1)

