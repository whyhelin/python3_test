#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from html.parser import HTMLParser
from urllib import request
from bs4 import BeautifulSoup
import requests


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    # 特殊字符有两种，
    # 一种是英文表示的 &nbsp;
    # 一种是数字表示的 &#1234;
    # 这两种字符都可以通过Parser解析出来。
    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

print('----------------------------------')


def bs_html():
    resp = requests.get('https://www.python.org/events/python-events/').text

    with request.urlopen('https://www.python.org/events/python-events/') as url:
        html = url.read().decode('utf-8')
    soup = BeautifulSoup(resp, 'html.parser')

    for li in soup.select('.list-recent-events > li'):
        print('-' * 50)
        print('会议名:\t\t%s' % li.find('a').text)
        print('会议时间:\t%s' % li.find('time').text)
        print('会议地点:\t%s' % li.select_one('.event-location').text)
    print('-' * 50)

bs_html()

print('----------------------------------------')


def regex_html():
    with request.urlopen('https://www.python.org/events/python-events/') as url:
        html = url.read().decode('utf-8')

    when = re.findall(r'<time\sdatetime=.{27}>(.+?)\s<span\sclass="say-no-more">\s(\d{4})</span></time>', html)
    what = re.findall(r'<h3\sclass="event-title"><a href=".+?">(.+?)</a></h3>', html)
    where = re.findall(r'<span\sclass="event-location">(.+?)</span>', html)
    result = []
    for i in range(len(when)):
        result.append({'datetime': when[i][0].replace('–', '-'), 'event-title': what[i], 'event-location': where[i]})

    for event in result:
        print('-' * 50)
        print('会议名:\t\t%s' % event.get('event-title'))
        print('会议时间:\t%s' % event.get('datetime'))
        print('会议地点:\t%s' % event.get('event-location'))
    print('-' * 50)

# regex_html()

print('----------------------------------------------')


class PythonEventHtmlParser(HTMLParser):
    events = []
    bool_title = False
    bool_time = False
    bool_place = False

    def handle_starttag(self, tag, attrs):
        # html 属性是一个list里嵌套的tuple
        # [('href', 'aa.html'), ('data-api', 'fooo'), ('class', 'nav btn')]
        if len(attrs) > 0:
            if tag == 'h3' and attrs[0][1] == 'event-title':
                self.bool_title = True
            if tag == 'time' and attrs[0][0] == 'datetime':
                self.bool_time = True
            if tag == 'span' and attrs[0][1] == 'event-location':
                self.bool_place = True

    def handle_endtag(self, tag):
        if tag == 'h3' and self.bool_title:
            self.bool_title = False
        if tag == 'time' and self.bool_time:
            self.bool_time = False
        if tag == 'span' and self.bool_place:
            self.bool_place = False

    def handle_data(self, data):
        global event
        if self.bool_title:
            event = {}
            event['event-title'] = data
        if self.bool_time:
            event['datetime'] = data
        if self.bool_place:
            event['event-location'] = data
            self.events.append(event)


def parse_python_events():
    parser = PythonEventHtmlParser()
    html = ''
    with request.urlopen('http://www.python.org/events/python-events') as f:
        html = f.read().decode('utf-8')
        print(html)
    parser.feed(html)

    events = parser.events
    for event in events:
        print('-' * 50)
        print('会议名:\t\t%s' % event.get('event-title'))
        print('会议时间:\t%s' % event.get('datetime'))
        print('会议地点:\t%s' % event.get('event-location'))
    print('-' * 50)


# parse_python_events()
