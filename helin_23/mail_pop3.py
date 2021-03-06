#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

# 第一步：用poplib把邮件的原始文本下载到本地；
# 第二部：用email解析原始文本，还原为邮件对象。

# 输入邮件地址, 口令和POP3服务器地址:
email = ''
password = ''
pop3_server = 'pop.qq.com'
global mailcontent


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            mailcontent.append('%s%s: %s' % ('  ' * indent, header, value))
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            mailcontent.append('%spart %s' % ('  ' * indent, n))
            mailcontent.append('%s--------------------' % ('  ' * indent))
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            mailcontent.append('%sText: %s' % ('  ' * indent, content))
            print('%sText: %s' % ('  ' * indent, content))
        else:
            mailcontent.append('%sAttachment: %s' % ('  ' * indent, content_type))
            print('%sAttachment: %s' % ('  ' * indent, content_type))


# 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server)

# 可以打开或关闭调试信息:
server.set_debuglevel(1)
print('----------------------------')

# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))
print('----------------------------')

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
# 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
count, size = server.stat()
# print('Messages: %s. Size: %s' % (count, size))
# print('----------------------------')

# 需要取出所有信件的头部，信件id是从1开始的。
# for i in range(1, count + 1):
    # 取出信件头部。注意：top指定的行数是以信件头为基数的，也就是说当取0行，
    # 其实是返回头部信息，取1行其实是返回头部信息之外再多1行。
    # mlist = server.top(i, 0)
    # print(mlist)
    # print('line: ', len(mlist[1]))

# list()返回所有邮件的编号:
# 列出服务器上邮件信息，这个会对每一封邮件都输出id和大小。不象stat输出的是总的统计信息
# resp, mails, octets = server.list()
# print(resp)
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
# print(mails)
# print(octets)
# print('----------------------------')

# 获取最新一封邮件, 注意索引号从1开始:
# index = len(mails)
# print(index)
# print('-----------------------------')


# 取第index封邮件完整信息，在返回值里，是按行存储在列表里的。resp是返回的状态信息
resp, lines, octets = server.retr(9)
# print(resp)
# print(lines)
# print(octets)
# print('-------------------------------')

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('gbk')
# print('--------------------------------')

# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
print(msg)
# print('---------------------------------')
mailcontent = []
print_info(msg)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)

with open('mail.txt', 'w', encoding='utf-8') as f:
    for s in mailcontent:
        f.write(s)

print(mailcontent)
mailcontent = []

# 关闭连接:
server.quit()


