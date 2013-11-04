# -*- coding:utf-8 -*-
import base64

s1 = base64.encodestring('helloworld')
s2 = base64.decodestring(s1)

print (s1, s2)

s = '我是字符串'
a = base64.b64encode(s)
print a
print base64.b64decode(a)