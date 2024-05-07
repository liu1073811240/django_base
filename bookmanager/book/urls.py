from django.urls import path, register_converter
from book.views import (index, create_book, shop, get, register,
                        json_data, method, response_test, json_response,
                        set_cookie, get_cookie, set_session, get_session,
                        login, LoginView, OrderView)

class MobileConverter:
    """自定义路由转换器：匹配手机号"""
    # 匹配手机号码的正则
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        # 将匹配结果传递到视图内部时使用
        return int(value)

    def to_url(self, value):
        # 将匹配结果用于反向解析传值时使用
        return str(value)


# 注册自定义路由转换器
# register_converter(自定义路由转换器, '别名')
register_converter(MobileConverter, 'mobile')

# 这个是固定写法 urlpatters = []
urlpatterns = [
    # path(路由，视图函数名)
    path('index/', index),
    path('create_book/', create_book),

    # path('<city_id>/<shop_id>/', shop),
    # path('<int:city_id>/<int:shop_id>/', shop),
    path('<int:city_id>/<mobile:shop_id>/', shop),  # 要求是电话号码格式

    path('get/', get),
    path('register/', register),
    path('json_data/', json_data),
    path('method/', method),
    path('response_test/', response_test),
    path('json_response/', json_response),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', login),

    # 类视图
    path('163login/', LoginView.as_view()),
    path('order/', OrderView.as_view())





]
