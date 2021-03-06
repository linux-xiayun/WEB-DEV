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
from django.views.generic.base import RedirectView

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^base$', views.base),
    url(r'^welcome$', views.welcome),
    url(r'^update$', views.Items_All),
    url(r'^windows_upd$', views.windows_upd, name='windows_upd'),
    url(r'^linux_upd$', views.linux_upd, name='linux_upd'),
    url(r'^add_items$', views.add_items, name='add_items'),
    url(r'^new_item/$', views.new_items),
    url(r'^q$', views.query),
    url(r'^delete$', views.delete_items),
    url(r'^itemdata_update$', views.itemdata_update),
    url(r'^itemdata_rollback$', views.itemdata_rollback),
    url(r'^asset/list/page=(\d+)$', views.assetList, name="asset_list"),
    url(r'^asset/add$', views.addAsset, name="asset_add"),
    url(r'^asset/edit$', views.editHostAsset, name="asset_edit"),
    url(r'^asset/action$', views.assetAction, name="asset_action"),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/img/favicon.ico')),
    url(r'^jenkins/$', views.jenkinsurl, name='jenkins'),
    url(r'^publish$', views.ansible_api, name='publish'),
    #url(r'^zabbix/$', views.zabbixurl, name='zabbix'),
    url(r'^gitlab/$', views.gitlaburl, name='gitlab'),
    url(r'^zabbix/$', views.zabbixurl, name='zabbix'),
    url(r'^test_admin/$', views.testadmin),
    url(r'^qrcode/(.+)$', views.generate_qrcode, name='qrcode'),

]

