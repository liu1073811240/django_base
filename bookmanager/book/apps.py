from django.apps import AppConfig

# **apps.py**文件用于配置当前子应用的相关信息。
class BookConfig(AppConfig):
    name = 'book'

    verbose_name = '图书管理'  # 此名字在Django提供的Admin管理站点中会显示
