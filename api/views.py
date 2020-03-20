from django.shortcuts import render,redirect,HttpResponse,reverse

# Create your views here.
from api import models
#展示Book表数据

def book_list(request):
    if request.method=="GET":
        Book_list = models.Book.objects.all()
        return render(request,"Book_List.html",{'Book_list':Book_list})
    else:
        pass
#增加Book表数据
def book_add(request):
    if request.method=="GET":
        return render(request,"Book_add.html")
    else:
        title = request.POST.get("title")
        pub_date = request.POST.get("pub_date")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        book_add = models.Book.objects.create(title=title,pub_date=pub_date,price=price,publish=publish)
        book_add.save()
        return redirect("/book_list")
#删除Book表数据

def book_delete(request,id):
    models.Book.objects.filter(id=id).delete()
    return redirect("/book_list/")
#修改Book表数据

def book_edit(request,id):
    if request.method=="GET":
        print(id)
        books_edit = models.Book.objects.get(id=id)
        return render(request,"Book_edit.html",{'books_edit':books_edit})
    else:

        title = request.POST.get("title")
        pub_date = request.POST.get("pub_date")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        models.Book.objects.filter(id=id).update(title=title,pub_date=pub_date,price=price,publish=publish)

        return redirect(reverse("book_list"))
