#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from helin_25.web_wsgi_hello import application2

# Python内置了一个WSGI服务器，这个模块叫wsgiref，
# 它是用纯Python编写的WSGI服务器的参考实现。
# 所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:

httpd = make_server('', 8000, application2)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

