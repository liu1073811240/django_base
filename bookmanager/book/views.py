from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# **views.py**文件用于编写Web应用视图。

"""
视图
所谓的视图其实就是python函数视图函数有2个要求:
1．视图函数的第一个参数就是接收请求。这个请求其实就是 HttpRequest的类对象
2。必须返回一个响应
.".
"""
#我们期望用户输入http://127.0.0.1:8000/index/
# 来访问视图函数

from book.models import BookInfo
def index(request):
    # return HttpResponse("OK")

    # 准备上下文，定义在字典中测试数据
    context = {'title': '测试模板处理数据'}

    # 在这里实现增删改查
    # books = BookInfo.objects.all()
    # print(books)

    # 将上下文交给模板中进行处理，处理后视图响应给客户端。
    return render(request, 'Book/index.html', context)

"""
终端执行 python manage.py shell

# 增加数据
from book.models import BookInfo
# 方式1
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
book.save()

# 方式2
# objects -- 相当于一个代理，实现增删改查
BookInfo.objects.create(
    name='测试开发',
    pub_date='2020-1-1',
    readcount=10
)

# 修改数据
方式1
select * from bookinfo where id=6
book = BookInfo.objects.get(id=6)
book.name = '运维开发入门'
book.save()

# 方式2
BookInfo.objects.filter(id=6).update(name='爬虫入门', commentcount=666)


# 删除数据
# 分为物理删除（这条记录的删除） 和逻辑删除（修改标记位 例如is_delete=False）
# 方式1
book = BookInfo.objects.get(id=9)
book.delete()

# 方式2
BookInfo.objects.get(id=8).delete()
BookInfo.objects.filter(id=9).delete()

# 查询数据
# get查询单一结果﹐如果不存在会抛出模型类.DoesNotExist异常。
try:
    book=BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all查询多个结果。
BookInfo.objects.all()

# count查询结果数量·
BookInfo.objects.all().count()
BookInfo.objects.count()

# 过滤查询
#实现SQL中的where功能·包括
#
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

#模型类名.objects.filter(属性名__运算符=值)   获取n个结果  n=0,1,2,. . .
#模型类名.objects.exclude (属性名__运算符=值)    获取n个结果  n=0,1,2,. . .
#模型类名.objects.get(属性名__运算符=值)    获取1个结果 或者 异常


"""




