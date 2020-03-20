"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,re_path
from api.views import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # #默认根目录访问跳转到login
    url('login/', views.login),

    url('^index/', views.index),

    url('^logout/', views.logout),

    # #有名分组
    # url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$',views.years_month),
    # #使用别名实现反向解析url,以此减少后期修改url造成的维护成本,前端调用{%url 'index'%}
    # url('login',views.login,name="login"),
    ################书籍管理#################
    url(r'^book_list/', views.book_list, name="book_list"),
    url(r'^book_add/', views.book_add, name="book_add"),
    url(r'^book_delete/', views.book_delete, name="book_delete"),
    url(r'^book_edit/(\d+)/$', views.book_edit, name="book_edit"),

    ################作者管理#################
    url(r'^author_list/', views.author_list, name="author_list"),
    url(r'^author_add/', views.author_add, name="author_add"),
    url(r'^author_delete/', views.author_delete, name="author_delete"),
    url(r'^author_edit/(\d+)/$', views.author_edit, name="author_edit"),

    ################出版社管理#################
    url(r'^publish_list/', views.publish_list, name="publish_list"),
    url(r'^publish_add/', views.publish_list, name="publish_add"),
    url(r'^publish_delete/', views.publish_list, name="publish_delete"),
    url(r'^publish_edit/(\d+)/$', views.publish_list, name="publish_edit"),
    ###################文件上传#################
    url(r'^context_upload/', views.context_upload, name="context_upload"),
    url(r'^ajax_upload/', views.ajax_upload, name="ajax_upload"),
]



















