from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from login.models import User
import sys
from .serializer import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import hashlib
# Create your views here.

#パスワードmd5暗号化
def md5(p1):
    m = hashlib.md5()
    m.update(p1.encode())
    return m.hexdigest()

#トップページ
def index(request):
    return render(request, 'index.html', locals())

def modify(request):
    uid = request.GET.get("uid")
    if request.method == 'POST':
        username = request.POST.get('username')
        realname = request.POST.get('realname')
        password = request.POST.get('password')
        py = request.POST.get('py')
        email = request.POST.get('email')
        user = User.objects.get(id=uid)
        user.username=username
        user.realname=realname
        if password:
            user.password=md5(password)
        user.py = py
        user.email = email
        user.save()
        return HttpResponseRedirect('/login/manage')
    else:
        user = User.objects.get(id=uid)
        return render(request, 'modify.html', locals())


def delete(request):
    uid = request.GET.get("uid")
    if uid:
        user = User.objects.filter(id=uid)
        user.delete()
        return HttpResponseRedirect('/login/manage')
    else:
        return HttpResponseRedirect('/login/manage')

def manage(request):
    py = request.GET.get("py")
    email = request.GET.get("email")
    if py :
        users = User.objects.filter(py__contains=py)
    elif email:
        users = User.objects.filter(email__contains=email)
    else:
        users = User.objects.all()

    return render(request, 'manage.html', locals())

#登録
def reg(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        realname = request.POST.get('realname')
        py = request.POST.get('py')
        email = request.POST.get('email')
        
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        try:
            user = User.objects.filter(username=username)
            if user:
                error_message = "用户名已存在"
                return render(request, 'reg.html', locals())
        except:
            print('error')

        if password_1 != password_2:
            error_message = "两次密码输入不一致"
            return render(request, 'reg.html', locals())
        else:
            user = User.objects.create(username=username, password=md5(password_1), realname=realname, py=py,email=email)
            request.session['username']=user.username
            request.session['uid']=user.id
            return HttpResponse('注册成功, <a href="/login/index">返回主页</a>')

    else:
        return render(request, 'reg.html', locals())
#ログアウト        
def logout(request):
    del(request.session['username'])
    del(request.session['uid'])
    return HttpResponseRedirect('/login/index')

#ログイン
# @api_view(['GET', 'POST'])
# api_viewで実装してみたい
def login(request):
    data = JSONParser().parse(request)
    # data2 = request.data
    # api_viewがエラーをださなければrequest.dataで中身がとれる　
    print(data)
    print(data.get("username"))
    print(data.get("password"))
    serializer_class = UserSerializer
    if request.method == 'POST':
        username = data.get('username')
        password = data.get('password')
        print(username)
        user = User.objects.filter(username=username).first()
        if user:
            password1 = md5(password)
            password2 = user.password
            
            if password1 == password2:
                request.session['username']=user.username
                request.session['uid']=user.id

                return HttpResponseRedirect('/login/index')
            else:
                error_message = "用户名或密码错误"
                return render(request, 'login.html', locals())

        else:
            error_message = "用户名或密码错误"
            return render(request, 'login.html', locals())
    else:
        print("else")
        return render(request, 'login.html', locals())


# def success(request):
#     return HttpResponse('---success---')
