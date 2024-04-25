from django.contrib import admin
from book.models import BookInfo, PeopleInfo

# Register your models here.
# **admin.py**文件跟网站的后台管理站点配置相关。

# 注册数据模型
admin.site.register(BookInfo)
# 注册人物模型
admin.site.register(PeopleInfo)
