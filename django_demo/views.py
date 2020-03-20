#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2020/3/14 0014 12:53
# from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
def years_month(request,year,month):

    return HttpResponse("year:%s,month:%s"%(year,month))


def index(request):

  s_info = ['香蕉','苹果','雪梨']
  import datetime
  date = datetime.datetime.now()

  return render(request,'index.html',{'sp':s_info,'date':date})

def login(request):

    if request.method =="GET":
        return render(request,"index.html")






















if __name__ == '__main__':
    pass