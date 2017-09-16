#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person
# 引入我们创建的表单类
from .forms import AddFrom

def index(request):
    IPaddr = request.META['REMOTE_ADDR']
    return HttpResponse("欢迎光临！welcome！%s" % IPaddr)

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def c2(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) * int(b)
    return HttpResponse(str(c))

def home(request):
    string = "狗狗无敌，瓦特上天！！！"
    return render(request, 'WTC/home.html', {'string': string})

def include_xiay(request):
    messages = Person.objects.filter(first_name__iexact="xia", last_name__iexact="yun").values('age')
    return HttpResponse(messages)

def add_int(request):
    if request.method == 'POST':# 当提交表单时
        form = AddFrom(request.POST)# form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:# 当正常访问时
        form = AddFrom()
    return render(request, 'WTC/add_2.html', {'form':form})


