"""First_Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from WTC import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^login$', views.login),
    url(r'^base$', views.base),
    url(r'^update$', views.update),
    url(r'^add/', views.add, name='add'),
    url(r'^add/(\d+)/(\d+)', views.c2, name='c2'),
    url(r'WTC/', views.home, name='WTC'),
    url(r'include_name/', views.include_xiay, name='name'),
    url(r'^add_2/', views.add_int, name='add_2'),
    url(r'^asset/list/page=(\d+)$', views.assetList, name="asset_list"),
    url(r'^asset/add$', views.addAsset, name="asset_add"),
    url(r'^asset/edit$', views.editHostAsset, name="asset_edit"),
    url(r'^asset/action$', views.assetAction, name="asset_action"),

]

