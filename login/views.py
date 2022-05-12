import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from login.models import Category, Product, User
import hashlib
from django.core.files.base import File
from rest_framework import viewsets
from .models import UserInfo
from .serializer import UserInfoSerializer

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
        if not username:
            error_message = "IDをご入力ください。"
            return render(request, 'reg.html', locals())
        realname = request.POST.get('realname')
        if not realname:
            error_message = "お名前をご入力ください。"
            return render(request, 'reg.html', locals())
        py = request.POST.get('py')
        if not py:
            error_message = "カタカナをご入力ください。"
            return render(request, 'reg.html', locals())
        email = request.POST.get('email')
        if not email:
            error_message = "メールアドレスをご入力ください。"
            return render(request, 'reg.html', locals())
        password_1 = request.POST.get('password_1')
        if not password_1:
            error_message = "パスワードを設定ください。"
            return render(request, 'reg.html', locals())
        password_2 = request.POST.get('password_2')
        if not password_2:
            error_message = "再度パスワードを入力ください。"
            return render(request, 'reg.html', locals())
        try:
            user = User.objects.filter(username=username)
            if user:
                error_message = "すでにアカウントが存在しています。"
                return render(request, 'reg.html', locals())
        except:
            print('error')

        if password_1 != password_2:
            error_message = "パスワードが一致されていません。"
            return render(request, 'reg.html', locals())
        else:
            user = User.objects.create(username=username, password=md5(password_1), realname=realname, py=py,email=email)
            request.session['username']=user.username
            request.session['uid']=user.id
            return HttpResponse('登録成功, <a href="/login/index">ホームへ</a>')

    else:
        return render(request, 'reg.html', locals())
#ログアウト        
def logout(request):
    del(request.session['username'])
    del(request.session['uid'])
    return HttpResponseRedirect('/login/index')

#ログイン
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        print(user)
        if user:
            password1 = md5(password)
            password2 = user.password
            
            if password1 == password2:
                request.session['username']=user.username
                request.session['uid']=user.id

                return HttpResponseRedirect('/login/index')
            else:
                error_message = "IDかパスワードが誤っています。"
                return render(request, 'login.html', locals())

        else:
            error_message = "IDかパスワードが誤っています。"
            return render(request, 'login.html', locals())
    else:
       
        return render(request, 'login.html', locals())


# def success(request):
#     return HttpResponse('---success---')

#密码修改
def change_pwd(request):
    if request.method == 'GET':
        # error_message = "请先登录。"
        try:
            if request.session['username']:
                print(request.session['username'])
                return render(request, 'change_pwd.html', locals())
            else:
                return render(request, 'index.html', locals())
        except:
            return render(request, 'index.html', locals())
    if request.method == 'POST':
        # username = request.session['username']
        username = request.session['username']
        print(username)
        if not username:
            return render(request, 'index.html', locals())
        old_password = request.POST.get('old_password')
        if not old_password:
            error_message = "古いパスワードをご入力ください。"
            return render(request, 'change_pwd.html', locals())

        password_1 = request.POST.get('password_1')
        if not password_1:
            error_message = "パスワードを設定ください。"
            return render(request, 'change_pwd.html', locals())
        password_2 = request.POST.get('password_2')
        if not password_2:
            error_message = "再度パスワードを入力ください。"
            return render(request, 'change_pwd.html', locals())
        try:
            user = User.objects.filter(username=username,password=md5(old_password)).first()
        except:
            print('error')
        if not user:
            error_message = "正しく古いパスワードをご入力ください。"
            return render(request, 'change_pwd.html', locals())
        elif password_1 != password_2:
            error_message = "パスワードが一致されていません。"
            return render(request, 'change_pwd.html', locals())
        else:
            user.password = md5(password_1)
            user.save()
            message = '修改成功。'
            return render(request, 'msg.html', locals())
    else:
        return render(request, 'reg.html', locals())

#商品登録
def product_add(request):
    if request.method == 'GET':
        # error_message = "请先登录。"
        try:
            if request.session['username']:
                print(request.session['username'])
                category_list = Category.objects.all()
                print('category_name:', category_list[0].category_name)
                return render(request, 'product_add.html', locals())
            else:
                return render(request, 'index.html', locals())
        except:
            return render(request, 'index.html', locals())
    if request.method == 'POST':
        # username = request.session['username']
        username = request.session['username']
        print(username)
        if not username:
            return render(request, 'index.html', locals())
        
        prod_name = request.POST.get('prod_name')
        if not prod_name:
            error_message = '请输入商品名'
            return render(request, 'product_add.html', locals())
        prod_desc = request.POST.get('prod_desc')
        if not prod_desc:
            error_message = '请输入商品描述'
            return render(request, 'product_add.html', locals())
        prod_price = request.POST.get('prod_price')
        if not prod_price:
            error_message = '请输入商品原价'
            return render(request, 'product_add.html', locals())
        prod_now_price = request.POST.get('prod_now_price')
        if not prod_now_price:
            error_message = '请输入商品现价'
            return render(request, 'product_add.html', locals())
        prod_num = request.POST.get('prod_num')
        if not prod_num:
            error_message = '请输入商品数量'
            return render(request, 'product_add.html', locals())
        pic1 = request.FILES.getlist('prod_pic1')
        if not pic1:
            error_message = '请输入商品图片'
            return render(request, 'product_add.html', locals())
        pic1 = pic1[0]
        print("pic1名称：", pic1.name)
        # prod_pic1 = request.FILES('prod_pic1')
        pic2 = request.FILES.getlist('prod_pic2')
        if pic2:
            pic2 = pic2[0]
        pic3 = request.FILES.getlist('prod_pic3')
        if pic3:
            pic3 = pic3[0]
        pic4 = request.FILES.getlist('prod_pic4')
        if pic4:
            pic4 = pic4[0]
        pic5 = request.FILES.getlist('prod_pic5')
        if pic5:
            pic5 = pic5[0]
        
        category_name = request.POST.get('category')
        category = Category.objects.get(category_name=category_name)
        print('%s, %s, %s, %s, %s, %s'%(prod_name, prod_desc, prod_price, prod_now_price, prod_num, category))
        Product.objects.create(
            prod_name=prod_name, 
            prod_desc=prod_desc,
            prod_price=prod_price,
            prod_now_price=prod_now_price,
            prod_num=prod_num,
            prod_pic1=pic1,
            prod_pic2=pic2,
            prod_pic3=pic3,
            prod_pic4=pic4,
            prod_pic5=pic5,
            category=category
            )
        return render(request, 'product_list.html', locals())


def product_list(request):
    product_list = Product.objects.all()
    # host = request.META['HTTP_HOST']
    # print(host)
    for product in product_list:
        # print(str(product.prod_pic1.file))
        product.prod_pic1 = '/login' + settings.MEDIA_URL + str(product.prod_pic1)
        if product.prod_pic2:
            print(type(product.prod_pic2))
        if product.prod_pic2:
            product.prod_pic2 = '/login' + settings.MEDIA_URL + str(product.prod_pic2)
        if product.prod_pic3:
            product.prod_pic3 = '/login' + settings.MEDIA_URL + str(product.prod_pic3)
        if product.prod_pic4:
            product.prod_pic4 = '/login' + settings.MEDIA_URL + str(product.prod_pic4)
        if product.prod_pic5:
            product.prod_pic5 = '/login' + settings.MEDIA_URL + str(product.prod_pic5)
    return render(request, 'product_list.html', locals())

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()

    serializer_class = UserInfoSerializer