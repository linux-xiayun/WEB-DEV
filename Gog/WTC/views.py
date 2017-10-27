#coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# 引入我们创建的表单类
from .forms import AddFrom
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings
from django.db.models import Q
from django.db import connection
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.template.context_processors import csrf
#import salt_api #,ssh_paramiko
import json
import re
import math

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# urllib.urlopen一个https的时候会验证一次SSL证书,当目标使用的是自签名的证书时就会抛出一个错误

table_name = 'web_access_count'
field_name = 'insert_time'
cursor = connection.cursor()

def index_2(request):
    IPaddr = request.META['REMOTE_ADDR']
    return HttpResponse("欢迎光临！welcome！%s" % IPaddr)

@login_required(login_url='login')
def base(request):
    username = request.COOKIES.get('username','')
    return render_to_response('base.html', {'username': username})

def welcome(request):
    username = request.COOKIES.get('username','')
    return render_to_response('welcome.html', {'username': username})

def update(request):
    username = request.COOKIES.get('username', '')
    return render_to_response('index.html',{'username':username})

def windows_upd(request):
    username = request.COOKIES.get('username', '')
    return render_to_response('update/windows.html',{'username':username})

def linux_upd(request):
    username = request.COOKIES.get('username', '')
    return render_to_response('update/linux.html',{'username':username})

def add_items(request):
    username = request.COOKIES.get('username', '')

    return render_to_response('update/items.html',{'username':username})

#def add(request):
#    a = request.GET.get('a', 0)
#    b = request.GET.get('b', 0)
#    c = int(a) + int(b)
#    return HttpResponse(str(c))

##def c2(request):
##    a = request.GET.get('a', 0)
##    b = request.GET.get('b', 0)
##    c = int(a) * int(b)
##    return HttpResponse(str(c))

###def home(request):
###    s###tring = "狗狗无敌，瓦特上天！！！"
###    return render(request, 'WTC/home.html', {'string': string})

#def include_xiay(request):
#    messages = Person.objects.filter(first_name__iexact="xia", last_name__iexact="yun").values('age')
#    return HttpResponse(messages)

#def add_int(request):
#    if request.method == 'POST':# 当提交表单时
#        form = AddFrom(request.POST)# form 包含提交的数据
#
#        if form.is_valid():# 如果提交的数据合法
#            a = form.cleaned_data['a']
#            b = form.cleaned_data['b']
#            return HttpResponse(str(int(a)+int(b)))
#    else:# 当正常访问时
#        form = AddFrom()
#    return render(request, 'WTC/add_2.html', {'form':form})


def login(request):
    if request.method == 'GET':
        return render_to_response('login.html',RequestContext(request))
    if request.method == 'GET':
        return render_to_response('login.html',RequestContext(request))
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('welcome')
            response.set_cookie('username', username)
            return response
        else:
            error = "用户名或密码错误，请重新输入。"
            return render_to_response("login.html",{'error':error},RequestContext(request))

# @login_required  #只有用户在登录的情况下才能调用该视图，否则将自动重定向至登录页面。
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('login')
    response.delete_cookie('username')
    return response

@login_required()
def assetList(request, page):
    pass
#    all_asset = AssetInfo.objects.all()
#    all_asset_info = []
#    for i in all_asset:
#        all_asset_info.append({
#            'id':i.id,
#            'public_ip':i.public_ip,
#            'intranet_ip':i.intranet_ip,
#            'host_name':i.host_name,
#            'os':i.os,
#            'cpu_model':i.cpu_model,
#            'cpu_thread_number':i.cpu_thread_number,
#            'memory':i.memory,
#            'disk':json.loads(str(i.disk).replace("'",'"').replace('u"','"')),  # 将unicode字符串转为字典，否则前端无法遍历
#            'minion_id':i.minion_id
#        })
#    total_record = len(all_asset_info)
#    if request.method == "GET":
#        page = int(page)
#        page_init = 5
#        # all_asset_info = AssetInfo.objects.all()
#        total_page = int(math.ceil(float(len(all_asset_info))/page_init))  # 进一法取整
#        total_page_sequence = [ i for i in range(total_page)]
#        start_page = page_init * page - page_init
#        end_page = page_init * page
#        asset_info = all_asset_info[start_page:end_page]
#        return render_to_response('asset/asset_list.html',{'asset_info': asset_info,
#                                                           'total_num': total_page_sequence,
#                                                           'page': page,
#                                                           'total_record':total_record}, RequestContext(request))
#    elif request.method == "POST":
#        search = request.POST.get('search')
#        if search:
#            result = all_asset.filter(Q(public_ip=search)|Q(intranet_ip=search)|Q(host_name=search))
#            search_result = []
#            for i in result:
#                search_result.append({
#                    'id':i.id,
#                    'public_ip':i.public_ip,
#                    'intranet_ip':i.intranet_ip,
#                    'host_name':i.host_name,
#                    'os':i.os,
#                    'cpu_model':i.cpu_model,
#                    'cpu_thread_number':i.cpu_thread_number,
#                    'memory':i.memory,
#                    'disk':json.loads(str(i.disk).replace("'",'"').replace('u"','"')),  # 将unicode字符串转为字典，否则前端无法遍历
#                    'minion_id':i.minion_id
#                })
#            if len(search_result) == 0 :
#                search_error = "请尝试公网IP/内网IP/主机名为查询条件!"
#                return render_to_response('asset/asset_list.html',{'search_error': search_error}, RequestContext(request))
#            return render_to_response('asset/asset_list.html',{'search_result': search_result}, RequestContext(request))
#        else:
#            search_error = "输入不能为空!"
#            return render_to_response('asset/asset_list.html',{'search_error': search_error}, RequestContext(request))
#
def addAsset(request):
    pass
#    minion_id = request.GET['minion']
#    if minion_id:
#        try:
#            addHostAsset(request, minion_id)
#            return HttpResponseRedirect('/asset/list/page=1')
#        except KeyError:
#            error = "Minion ID不存在或者无法连接！"
#            all_asset_info = AssetInfo.objects.all()
#            return render_to_response('asset/asset_list.html', {'error': error,'all_asset_info': all_asset_info})
#    else:
#        error = "输入不能为空！"
#        all_asset_info = AssetInfo.objects.all()
#        return render_to_response('asset/asset_list.html', {'error': error,'all_asset_info': all_asset_info})
#
@login_required()
def editHostAsset(request):
    pass#
#    # if request.method == "GET":
#    #     return HttpResponseRedirect('/asset/list/page=1')
#    if request.method == "POST":
#        id = request.POST.get('id')
#        update = AssetInfo.objects.get(id=id)
#        update.intranet_ip = request.POST.get('public_ip')
#        update.intranet_ip = request.POST.get('intranet_ip')
#        update.host_name = request.POST.get('host_name')
#        update.os = request.POST.get('os')
#        update.cpu_model = request.POST.get('cpu_model')
#        update.cpu_thread_number = request.POST.get('cpu_thread_number')
#        update.memory = request.POST.get('memory')
#        update.disk = request.POST.get('disk')
#        update.save()
#
#        return HttpResponseRedirect('/asset/list/page=1')

def addHostAsset(request, tgt):
    pass
#    sapi = salt_api.HostInfo()
#    host_asset = sapi.assetInfo(tgt)
#    # match_ip = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', tgt)
#    match_id = re.findall(r'^\d+$', tgt)
#    # 如果传入的tgt值是IP就以IP为查询添加，否则以minion id为查询条件。有记录就更新，无就插入
#    try:
#        # if match_ip:
#        #     update = AssetInfo.objects.get(public_ip=tgt)
#        if match_id:
#            update = AssetInfo.objects.get(id=tgt)
#        else:
#            update = AssetInfo.objects.get(minion_id=tgt)
#        update.intranet_ip = host_asset['intranet_ip']
#        update.host_name = host_asset['host_name']
#        update.os = host_asset['os']
#        update.cpu_model = host_asset['cpu_model']
#        update.cpu_thread_number = host_asset['cpu_thread_number']
#        update.memory = host_asset['memory']
#        update.disk = host_asset['disk']
#        update.minion_id = host_asset['minion_id']
#        update.save()
#    except:
#        insert = AssetInfo.objects.create(
#            public_ip=host_asset['public_ip'],
#            intranet_ip = host_asset['intranet_ip'],
#            host_name = host_asset['host_name'],
#            os = host_asset['os'],
#            cpu_model = host_asset['cpu_model'],
#            cpu_thread_number = host_asset['cpu_thread_number'],
#            memory = host_asset['memory'],
#            disk = host_asset['disk'],
#            minion_id = host_asset['minion_id'],
#        )
#        insert.save()
#    # return HttpResponseRedirect('/asset/list/page=1')

def delHostAsset(request, id):
    pass#
#    if isinstance(id, unicode_literals):
#        AssetInfo.objects.get(id=id).delete()
#        # return HttpResponseRedirect('/asset/list')
#    elif isinstance(id, list):
#        for id in id:
#            AssetInfo.objects.get(id=id).delete()
#        # return HttpResponseRedirect('/asset/list')

@login_required()
## 按钮操作
def assetAction(request):
    pass
#    if request.method == "GET":
#        #return HttpResponseRedirect('/asset/list/page=1')
#        return HttpResponseRedirect('/base')
#    if request.method == "POST":
#        # 点击哪个按钮就会传过来那个值。另外调用函数时不用写render，在调用的函数里面写或window.location.href
#        for key in request.POST:
#            if key == "del_id":
#                id = request.POST[key]
#                delHostAsset(request, id)
#            elif key == "refresh_mid":
#                mid = request.POST[key]
#                addHostAsset(request, mid)
#                # return HttpResponseRedirect('/asset/list/page=1')
#            # body: all_id%5B%5D=12&all_id%5B%5D=13
#            elif request.body.startswith("del_all_id"):
#                id_list = request.POST.getlist("del_all_id[]")   # 获取字典中的列表
#                delHostAsset(request, id_list)
#            elif request.body.startswith("refresh_all_id"):
#                id_list = request.POST.getlist("refresh_all_id[]")
#                for id in id_list:
#                    addHostAsset(request, id)
#                # return HttpResponseRedirect('/asset/list')

def Items_All(request):
    items_all = Update_items.objects.all()
    items_all_info = []
    if len(items_all_info) > 0:
        for i in items_all:
            items_all_info.append({
                'id':i.id,
                'name':i.items_name,
                'place':i.items_place,
                'system':i.items_system,
                'resource':i.items_resource,
            })
    else:
        items_all_info.append("'It's Null!")
    return HttpResponse(items_all_info)

@csrf_exempt
def new_items(request):
    if request.method == 'POST':
        items_name = request.POST.get('items_name')
        items_place = request.POST.get('items_place')
        items_system = request.POST.get('items_system')
        items_resource = request.POST.get('items_resource')
        item = Update_items()
        if len(items_name) > 0:
            item.items_name = items_name
            item.items_place = items_place
            item.items_system = items_system
            item.items_resource = items_resource
            item.save()
            messages = "添加成功！"
            return render(request, 'update/items.html', {'messages':messages})
        else:
            messages = "不能为空！"
            return render(request, 'update/items.html', {'messages':messages})

