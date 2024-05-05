from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
import json

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

def create_book(request):
    book = BookInfo.objects.create(
        name='redis基本入门',
        pub_date='2000-1-1',
        readcount=10
    )

    return HttpResponse("create")

def shop(request, city_id, shop_id):


    return JsonResponse({'city_id': city_id, 'shop_id': shop_id})

# /get/?a=1&b=2&a=3
def get(request):
    query_params = request.GET
    print(query_params)

    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)  # 3
    print(b)  # 2
    print(alist)  # ['1', '3']
    return HttpResponse('OK')


def register(request):
    data = request.POST
    print(data)

    a = request.POST.get('username')
    b = request.POST.get('password')
    alist = request.POST.getlist('username')
    print(a)
    print(b)
    print(alist)

    return HttpResponse('OK')

def json_data(request):
    # json数据 不能通过request.POST获取数据
    json_str = body = request.body
    print(body)

    json_str = json_str.decode()  # python3.6 无需执行此步
    print(json_str)
    req_data = json.loads(json_str)
    print(req_data)

    # 请求头
    print(request.META)
    print(request.META['CONTENT_TYPE'])  # 请求格式

    return HttpResponse('json')

def method(request):

    print(request.method)
    return HttpResponse('method')

def response_test(request):
    # return HttpResponse('res', status=300)

    response = HttpResponse('itcast')
    response.status_code = 400
    response['itcast'] = 'Python'
    return response

def json_response(request):
    info = {
        'name': 'itcast',
        'address': 'shunyi'
    }
    girl_friends = [
        {
            'name': 'itcast',
            'address': 'shunyi'
        },
        {
            'name': 'jack',
            'address': 'changping'
        }
    ]

    # data 返回的响应数据 一般是字典类型
    # response = JsonResponse(data=info)
    # response = JsonResponse(data=girl_friends, safe=False)

    import json
    data = json.dumps(girl_friends)
    response = HttpResponse(data)

    # return response

    # 重定向
    return redirect('http://www.itcast.com')


# http://192.168.18.128:8000/set_cookie/?username=itcast&password=123
def set_cookie(request):
    # 1. 获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 2. 服务器设置cookie信息
    # 通过响应对象.set_cookie方法
    response = HttpResponse('set_cookie')
    # key, value=''
    # man_age 是一个从秒数 响应开始 计数的一个秒数。
    response.set_cookie('name', username, max_age=60*60)
    response.set_cookie('password', password)

    response.delete_cookie('name')

    return response

def get_cookie(request):
    # 获取cookie
    print(request.COOKIES)
    name = request.COOKIES.get('name')

    return HttpResponse(name)

# session 是保存在服务器端, 数据相对安全
# session需要依赖于cookie

"""
第一次请求http://127.0.0.1:8000/set_session/?username=itheima·
我们在服务器端设置sesison信息服务器同时会生成一个sessionid的cookie信息·
浏览器接收到这个信息之后﹖会把cookie数据保存起来

第二次及其之后的请求都会携带这个sessionid．服务器会验证这个sessionid，验证没有问题会读取相关数据·实现业务逻辑

"""

def set_session(request):
    # 1. 模拟获取用户信息
    username = request.GET.get('username')
    # 2. 设置session信息
    # 假设我们通过模型查询到了用户的信息
    user_id = 1

    request.session['user_id'] = user_id
    request.session['username'] = username

    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{}.{}'.format(user_id, username)

    return HttpResponse(content)

