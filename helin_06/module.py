#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PIL import Image


# 有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
im = Image.open('E:\\study\\python\\python3.5Workspace\\test\\helin_06\\cat.jpg')
print(im.format, im.size, im.mode)
im.rotate(45).show()
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')