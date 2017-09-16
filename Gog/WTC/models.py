#coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_date = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
 
    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
 
    full_name = property(my_property)
