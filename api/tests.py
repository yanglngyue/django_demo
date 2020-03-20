from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_demo.settings")# project_name 项目名称
django.setup()

# Create your tests here.

from api import models
from django.db.models import Avg,Count,Max,Min
# book_add = models.Book.objects.create(title="西去取经的第三天",price=160,publish="沙河出版社",state=0,pub_date="2020-03-15")
# book_add.save()

# book_edit = models.Book.objects.filter(title='西去取经的第五天')
# # print(book_edit[0].title)
# print(book_edit)
# for i in book_edit.values():
#     print(i)

# < 1 > all(): 查询所有结果
# book_list = models.Book.objects.all()
# print(book_list)
# # < 2 > filter(**kwargs): 它包含了与所给筛选条件相匹配的对象
# book_list1 = models.Book.objects.all().filter(title='python')
# print(book_list1)
# # < 3 > get(**kwargs): 返回与所给筛选条件相匹配的对象，返回结果有且只有一个，
# # 如果符合筛选条件的对象超过一个或者没有都会抛出错误。
# book_list5 = models.Book.objects.all().get(title='python')
# print(book_list5)
# # < 4 > exclude(**kwargs): 它包含了与所给筛选条件不匹配的对象
# book_list6 = models.Book.objects.all().exclude(title='python')
# print(book_list6)
# # < 5 > order_by(*field): 对查询结果排序,默认升序，降序加“-”
# book_list7 = models.Book.objects.all().order_by("-price")
# print(book_list7)
# # < 6 > reverse(): 对查询结果反向排序
# book_list8 = models.Book.objects.all().order_by("price").reverse()
# print(book_list8)
# # < 8 > count(): 返回数据库中匹配查询(QuerySet)
# # 的对象数量。
# book_list9 = models.Book.objects.all().count()
# print(book_list9)
# # < 9 > first(): 返回第一条记录
# book_list3= models.Book.objects.all().first()
# print(book_list3)
# # < 10 > last(): 返回最后一条记录
# book_list4= models.Book.objects.all().last()
# print(book_list4)
# # < 11 > exists(): 如果QuerySet包含数据，就返回True，否则返回False
# book_list10= models.Book.objects.all().exists()
# print(book_list10)
# # < 12 > values(*field): 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
# # model的实例化对象，而是一个可迭代的字典序列
#
#
# book_list11= models.Book.objects.all().values("title","price")
# print(book_list11)
# # < 13 > values_list(*field): 它与values()
# # 非常相似，它返回的是一个元组序列，values返回的是一个字典序列
# book_list12= models.Book.objects.all().values_list("title","price")
# print(book_list12)
# # < 14 > distinct(): 从返回结果中剔除重复纪录
# book_list14= models.Book.objects.all().values_list("title","price").count()
# book_list15= models.Book.objects.all().values_list("title","price").distinct().count()
# book_list13= models.Book.objects.all().values_list("title","price").distinct()
# print(book_list13)
# print(book_list14)
# print(book_list15)
#
# book_list17= models.Book.objects.filter(pub_date__year=2012)
# print(book_list17)


#一对多添加记录
#方式1：
# book_add = models.Book.objects.create(title="python",price=122,pub_date='2012-12-12',publish_id=5)
# book_add.save()
#方式2：
# book_obj=models.Book.objects.create(title="金瓶眉",pub_date="2012-12-16",price=100,publish_id=6)
# book_obj.save()

#多对多添加记录
# book_obj=models.Book.objects.create(title="linux",pub_date="2012-12-18",price=100,publish_id=6)
# book_obj.save()
# alex1 = models.Author.objects.filter(name='alex')
egon1 = models.Author.objects.filter(name='egon')
# alex = models.Author.objects.filter(name='alex').first()

# egon2 = models.Author.objects.all()
# egon3 = models.Author.objects.all().first()
# egon = models.Author.objects.filter(name='egon').first()
# print(egon1)
# print(egon)
# print(egon2)
# print(egon3)
#基于对象的查询
"""

一对多查询
关联属性在book
Book--------------->Publish
正向查询：book.publish.name
反向查询：pub.book_set.all()





"""


#查询追风筝的人的出版社,正向查询
book = models.Book.objects.filter(title="追风筝的人").first()
print(book.publish.name)
#查询河南出版社出版的所有书籍，反向查询
pub = models.Publish.objects.filter(name="河南出版社").first()
print(pub.book_set.all())


"""

多对多查询
关联属性在book
Book--------------->Author
正向查询：book1.authors.all()
反向查询：author.book_set.all()





"""
#查询如何使用挖掘机炒菜的作者
book1 = models.Book.objects.filter(title="如何使用挖掘机炒菜").first()
print(book1.authors.all().values("age"))

#查询wu吴承恩写了那些书籍
author = models.Author.objects.filter(name="wu吴承恩").first()
print(author.book_set.all())



"""

一对一查询
关联属性在Author
Author--------------->AuthorDetail
正向查询：book1.authors.all()
反向查询：author.book_set.all()


"""
#查询太上老君的地址
auth = models.Author.objects.filter(name="太上老君").first()
print(auth.ad.addr)


#查询大红门18号路住的作者的电话

# au_detil = models.AuthorDetail.objects.filter(addr="大红门18号路").first()
#
# print(au_detil.author.email)



#
# publish_list = models.Publish.objects.all()
# for i in publish_list:
#     print(i.name)


utal_obj = models.Author.objects.filter(id=1).values("ad_id").first()
print(utal_obj)

#基于下划线的查询
#查询追风筝的人的出版社的名字

boo_name = models.Book.objects.filter(title="python").values("publish__name")
print(boo_name)
#查询河南出版社出版的所有书籍，反向查询
pub = models.Book.objects.filter(publish__name="河南出版社")
print(pub)

#查询如何使用挖掘机炒菜的作者
author = models.Book.objects.filter(title="如何使用挖掘机炒菜").values("authors__name")
print(author)

#查询wu吴承恩写了那些书籍
wu = models.Book.objects.filter(authors__name="wu吴承恩")
print(wu)

#查询太上老君的地址

addr = models.Author.objects.filter(name="太上老君").values("ad__addr")
print(addr)
#手机号183开头的作者出版过的所以书籍名称和出版社名称

obj = models.Book.objects.filter(authors__ad__tel__startswith="183").values_list("title","publish__name").distinct()
print(obj)
#聚合
count = models.Book.objects.all().aggregate(Count("id"))
print(count)

age = models.Author.objects.all().aggregate(Avg("age"))
print(age)

max = models.Author.objects.all().aggregate(max = Max("age"))

print(max)

#分组
#查询每一个作者的名称以及对应员工的平均年龄
oder_by = models.Author.objects.values("name").annotate(Avg("age"))
print(oder_by)


#跨表分组
# 查询每一个出版社的名称以及对应的书籍平均价格

object = models.Publish.objects.values("name").annotate(Avg("book__price"))
print(object)


# 查询每一个作者的名字以及出版的书籍的最高价格
author = models.Author.objects.values_list("name").annotate(Max("book__price"))

print(author)

# 查询每一个书籍的名称以及对应的作者的个数

cou = models.Book.objects.values_list("title").annotate(Count("authors__name"))

print(cou)

cou1 = models.Book.objects.annotate(t = Count("authors__id")).values_list("title","t")
print(cou1)
#统计不止一个作者的图书：

cou2 = models.Book.objects.annotate(t = Count("authors__id")).filter(t__gt=1).values_list("title","t")
print(cou2)

#查询价格大于300或评论数大于3000的书籍
from django.db.models import F,Q
# ret = models.Book.objects.filter(Q(price__gt=300)|Q(comment_count__gt=3000))
# # print(ret)

ret = models.Book.objects.filter(Q(price__gt=300)&Q(comment_count__gt=3000))
print(ret)

# for i in range(1,500):
#     models.Book.objects.create(title="book%s"%i,pub_date="2020-03-16 00:00:00.000000",price=100,publish_id=2,comment_count=5000,poll_count=100)









