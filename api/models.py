from django.db import models

# Create your models here.



class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32,null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2) # 999999.99
    comment_count = models.IntegerField(default=200)#评论数
    poll_count = models.IntegerField(default=100)#点赞数
    pub_date=models.DateTimeField()  # "2012-12-12"
    publish=models.ForeignKey(to="Publish",on_delete=models.CASCADE)  # 级联删除
    authors=models.ManyToManyField(to="Author")
    def __str__(self):
        return self.title


class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,null=True)
    email=models.CharField(max_length=32,null=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,null=True)
    pwd = models.CharField(max_length=32, null=True)
    age=models.IntegerField()
    email=models.CharField(max_length=32,null=True)
    ad=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    addr=models.CharField(max_length=32)
    tel=models.CharField(max_length=32)
    #author=models.OneToOneField("Author",on_delete=models.CASCADE)
    def __str__(self):
        return self.addr


#员工表
class Emp(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=20)
    dep=models.CharField(max_length=32)#部门
    pro=models.CharField(max_length=32)#省份
    salary=models.DecimalField(max_digits=8,decimal_places=2)
# class Author2Book(models.Model):
#     nid = models.AutoField(primary_key=True)
#     book=models.ForeignKey(to="Book",on_delete=models.CASCADE)
#     author=models.ForeignKey(to="Author",on_delete=models.CASCADE)hor = models.ForeignKey(to="Author",on_delete=models.CASCADE)