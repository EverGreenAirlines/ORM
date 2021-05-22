from django.shortcuts import render,HttpResponse

# Create your views here.
from app01.models import Book

def index(request):
    # =====================================添加记录=============================================================
    # #方式一：
    book_obj=Book(id=1, title="python宝典",state=True,price=100,pub_date="2020-12-21",publisher='人民出版社')
    book_obj.save()
    book_obj=Book(title="吸星大法", state=True,price=200,  pub_date="2018-12-12",publisher="明教出版社")
    book_obj.save()
    book_obj=Book(title="Python精华", state=True,price=230,  pub_date="2021-12-22",publisher="道教出版社")
    book_obj.save()

    # 方式二：
    book_obj=Book.objects.create(title="python入门",state=True,price=150,pub_date="2020-02-21",publisher="福建出版社")
    book_obj=Book.objects.create(title="独孤九剑", state=True,price=250,  pub_date="2018-03-12",publisher="华山出版社")
    book_obj=Book.objects.create(title="VBA指南", state=True,price=380,  pub_date="2021-11-18",publisher="泰山出版社")
    book_obj=Book.objects.create(title="Python指南", state=True,price=150,  pub_date="2019-01-12",publisher="衡山出版社")

    # =====================================查询记录API=============================================================
    '''
    1.方法调用者
    2.方法返回值
    :param request:
    :return:
    '''
    # (1)all(): 调用者:queryset对象， 返回值：queryset对象
    book_list=Book.objects.all()
    print('all()查询结果集：',book_list)
    book_list=Book.objects.all()[2]
    print('ll()[2]查询结果集索引为2：',book_list.publisher)

    # (2)first(),last(): 调用者:queryset对象， 返回值：model对象
    book_list = Book.objects.all().first()
    print('first()查询结果集首条书名：',book_list.title)
    book_list = Book.objects.all().last()
    print('last()查询结果集末条出版社名：',book_list.publisher)

    # (3)filter(): 调用者:queryset对象， 返回值：query对象
    book_list = Book.objects.filter(price=150)
    print('条件过滤filter(price=150)查询结果：',book_list)

    # (4)exclude(): 调用者:queryset对象， 返回值：query对象
    book_list = Book.objects.exclude(price=150)
    print('书价exclude(price=150)除外查询结果：',book_list)

    # (5)get(): 有且仅有一条查询结果才有意义 调用者:queryset对象， 返回值：model对象
    book_list = Book.objects.get(price=100)
    print('书价get(price=100)查询结果：',book_list.price)

    # (6)order_by():  调用者:queryset对象， 返回值：query对象
    book_list = Book.objects.all().order_by('-price')
    print('order_by(“-price”)查询结果集按价格倒叙：',book_list)

    # (7)reverse():  调用者:queryset对象， 返回值：query对象
    book_list = Book.objects.all().order_by('-price').reverse()
    print('reverse()查询结果集按价格倒叙再倒叙：',book_list)

    # (7)count():  调用者:queryset对象， 返回值：int
    book_list = Book.objects.all().count()
    print('count()查询结果计数为：',book_list)

    # (8)exists():  调用者:queryset对象， 返回值：bool
    book_list = Book.objects.all().exists()
    print('exists()查询结果集有否记录：',book_list)

    # (9)values():  调用者:queryset对象， 返回值：queryset-列表字典
    book_list = Book.objects.all().values('title','publisher')
    print('values(“title”,“publisher”)查询结果集按书名与出版社字典格式显示：',book_list)

    # (10)values_list():  调用者:queryset对象， 返回值：queryset-列表元组
    book_list = Book.objects.all().values_list('title','publisher')
    print('values_list(“title”,“publisher”)查询结果集按书名与出版社元组格式显示：',book_list)

    # (11)distinct():  调用者:queryset对象， 返回值：queryset-列表元组
    book_list = Book.objects.all().values('price').distinct()
    print('distinct()查询结果集去重：',book_list)

    # =====================================模糊查询记录API=============================================================
    book_list = Book.objects.filter(price__gt=150)
    print('price__gt=150书价格大于等于150查询结果集：',book_list[0].title)

    book_list = Book.objects.filter(title__icontains='h')
    print('title__icontains="h"书名包含h查询结果集：',book_list[1].title)

    book_list=Book.objects.filter(price__in=[100, 200, 300])
    print('书价格为100|200|300查询结果集：', book_list)
    book_list=Book.objects.filter(price__gt=100)
    print('书价格大于100查询结果集：', book_list)
    book_list=Book.objects.filter(price__lte=150)
    print('书价格小于等于150查询结果集：', book_list)
    book_list=Book.objects.filter(price__range=[100, 200])
    print('书价格为100到200查询结果集：', book_list)
    book_list=Book.objects.filter(title__contains="py")
    print('书名包含py查询结果集：', book_list)
    book_list=Book.objects.filter(title__icontains="py")
    print('书名包含py查询结果集：', book_list)
    book_list=Book.objects.filter(title__startswith="py")
    print('书名指定py开头查询结果集：', book_list)
    book_list=Book.objects.filter(pub_date__year=2020)
    print('出版年份指定2020查询结果集：', book_list,book_list.first().publisher)

    # =====================================删除和修改记录API=============================================================
    bookset=Book.objects.filter(title__icontains='py').delete()
    print(bookset)

    bookset = Book.objects.filter(price=200).update(price=250)
    print(bookset)

    bookset = Book.objects.all().update(title='毛泽东文选')
    print(bookset)



    return HttpResponse('OK')