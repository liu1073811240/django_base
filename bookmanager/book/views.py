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

def index(request):
    # return HttpResponse("OK")

    # 准备上下文，定义在字典中测试数据
    context = {'title': '测试模板处理数据'}

    # 将上下文交给模板中进行处理，处理后视图响应给客户端。
    return render(request, 'Book/index.html', context)
