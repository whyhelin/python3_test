#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def application1(environ, start_response):
    # for k, v in environ:
    #     print(k + ':' + v)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


def application2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>%s,Hello, %s!</h1>' % (environ['REQUEST_METHOD'], environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

