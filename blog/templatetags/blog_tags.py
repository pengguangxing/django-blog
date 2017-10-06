# -*- coding: utf-8 -*-
"""自定义模板标签的模块
   使用方式是在模板开头先导入本模块，使用标签：
   base.html
   {% load blog_tags %}
   ...
   <h3 class="widget-title">最新文章</h3>
       {% get_recent_posts as recent_post_list %}
"""
from django import template
from ..models import Post, Category


# 实例化一个 template.Library 类
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    """自定义的显示最近5篇文章的模板标签，可以直接在模板中使用"""
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    """归档的模板标签。
    dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，且是 Python 的 date 对象，
    精确到月份，降序排列。
    """
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
