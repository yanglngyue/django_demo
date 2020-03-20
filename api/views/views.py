from django.shortcuts import render,redirect,HttpResponse,reverse
import json
# Create your views here.
from api import models

from utils import pager
#展示Book表数据



def login(request):
    if request.method =="GET":
        return render(request,'login.html')
    else:
        res = {'user':None,'error':""}
        user = request.POST.get("user")
        password = request.POST.get("pwd")
        user_obj = models.Author.objects.filter(name=user,pwd=password).first()
        if user_obj:
            res['user'] = user
            return HttpResponse(json.dumps(res))
        else:
            res['error'] = "登录失败"
            return HttpResponse(json.dumps(res))


def index(request):

    return render(request,'index.html')

################################书籍管理实现#####################################
def book_list(request):
    if request.method=="GET":

        all_count = models.Book.objects.all().count()
        page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'Book_List.html', 11)
        Book_list = models.Book.objects.all()[page_info.start():page_info.end()]


        return render(request,"Book_List.html",{'Book_list':Book_list,'page_info':page_info})


#增加Book表数据
def book_add(request):
    if request.method=="GET":
        publish_list = models.Publish.objects.all()
        author_list = models.Author.objects.all()
        return render(request,"Book_add.html",{'publish_list':publish_list,'author_list':author_list})
    else:
        title = request.POST.get("title")
        pub_date = request.POST.get("pub_date")
        price = request.POST.get("price")
        # publish = request.POST.get("publish")
        publish = request.POST.get("publish")
        author = request.POST.getlist("author")
        print(publish,author)

        book_add = models.Book.objects.create(title=title,pub_date=pub_date,price=price,publish_id=publish)

        book_add.authors.add(*author)

        return redirect("/book_list")
#删除Book表数据

def book_delete(request):

    id = request.POST.get("id",None)
    if id:
        models.Book.objects.filter(id=id).delete()
        return HttpResponse("ok")
    else:
        return HttpResponse("not ok")
#修改Book表数据

def book_edit(request,id):
    books_edit = models.Book.objects.get(id=id)
    if request.method=="GET":


        publish_list = models.Publish.objects.all()
        author_list = models.Author.objects.all()

        return render(request,"Book_edit.html",{'books_edit':books_edit,'publish_list':publish_list,'author_list':author_list})
    else:

        title = request.POST.get("title")
        pub_date = request.POST.get("pub_date")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        author = request.POST.getlist("author")
        models.Book.objects.filter(id=id).update(title=title,pub_date=pub_date,price=price,publish_id=publish)
        books_edit.authors.set(author)

        return redirect(reverse("book_list"))


################################作者管理实现#####################################
#查看列表
def author_list(request):
    all_count = models.Author.objects.all().count()
    page_info = pager.PageInfo(request.GET.get('page'), all_count, 10, 'author_list.html', 11)
    author_obj = models.Author.objects.all()[page_info.start():page_info.end()]

    return render(request,'author_list.html',{'author_obj':author_obj,'page_info':page_info})
#增
def author_add(request):
    if request.method =="GET":
        author_obj = models.Author.objects.all()
        return render(request, 'author_add.html')
    else:

        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        # publish = request.POST.get("publish")
        addr = request.POST.get("addr")
        tel = str(request.POST.get("tel"))

        print(addr,tel)
        autal_add = models.AuthorDetail.objects.create(addr=addr, tel=tel)
        autal_add.save()

        autal_obj = models.AuthorDetail.objects.filter(addr=addr).first()

        au_add= models.Author.objects.create(name=name, age=age, email=email,ad=autal_obj)

        au_add.save()



        return redirect(reverse('author_list'))



#删
def author_delete(request):
    id = request.POST.get("id",None)
    print(id)
    if id:
        models.Author.objects.filter(id=id).delete()

        return HttpResponse("ok")
    else:
        return HttpResponse("not ok")

#改
def author_edit(request,id):
    author_obj = models.Author.objects.filter(id=id).first()
    if request.method =="GET":



        return render(request,'author_edit.html',{'author_obj':author_obj})
    else:

        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        # publish = request.POST.get("publish")
        addr = request.POST.get("addr")
        tel = str(request.POST.get("tel"))

        Au_id = models.Author.objects.filter(id=id).filter().values("ad_id")
        print(Au_id[0]["ad_id"])
        models.AuthorDetail.objects.filter(id=Au_id[0]["ad_id"]).update(addr=addr, tel=tel)

        models.Author.objects.filter(id=id).update(name=name, age=age, email=email )




        return redirect(reverse('author_list'))





################################出版社管理实现#####################################

#查看列表
def publish_list(request):
    pass
#增
def publish_add(request):
    pass


#删
def publish_delete(request,id):
    pass

#改
def publish_edit(request,id):
    pass

################################文件上传#####################################
import os
from django_demo import settings
def context_upload(request):
    if request.method =="GET":
        return render(request, 'context_upload.html')
    else:

        file_obj = request.FILES.get('upload_form')

        print(request.FILES)
        print(file_obj)
        print(type(file_obj))
        print(file_obj.name)
        print(type(file_obj.name))
        path_name = file_obj.name
        # print(path_name)

        path_name = os.path.join(settings.BASE_DIR, "media", "img", path_name)
        print(path_name)
        with open(path_name,'wb') as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse("ok")





def ajax_upload(request):
    if request.method =="GET":
        return render(request,'ajax_upload.html')
    else:
        file_obj = request.FILES.get("upload_ajax")
        print(request.FILES)
        # print(file_obj)
        # print(type(file_obj))
        print(file_obj.name)
        print(type(file_obj.name))

        path_name =file_obj.name

        path_name = os.path.join(settings.BASE_DIR,"media","img",path_name)
        with open(path_name,'wb') as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse("ok")
















