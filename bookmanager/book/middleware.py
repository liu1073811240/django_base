
# 导入中间件的父类
from django.utils.deprecation import MiddlewareMixin

class TestMiddleware1(MiddlewareMixin):
    """自定义中间件"""
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request1被调用')
        # username = request.COOKIES.get('username')
        # if username is None:
        #     print('没有用户信息')
        # else:
        #     print('有用户信息')

    def process_view(self, request, view_func, view_args, view_kwargs):
        """处理视图前自动调用"""
        print('process_view1被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response1被调用')
        return response

class TestMiddleware2(MiddlewareMixin):
    """自定义中间件"""
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request2被调用')
        # username = request.COOKIES.get('username')
        # if username is None:
        #     print('没有用户信息')
        # else:
        #     print('有用户信息')

    def process_view(self, request, view_func, view_args, view_kwargs):
        """处理视图前自动调用"""
        print('process_view2被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response2被调用')
        return response