# -*- coding:utf-8 -*-

'''
在开发自用爬虫过程中，有的网页是utf-8，有的是gb2312,有的是gbk，怎么办？
python从零基础到网页采集培训
下面所说的都是针对python2.7
如果不加处理，采集到的都是乱码，解决的方法是将html处理成统一的utf-8编码。
'''
#chardet 需要下载安装
#import chardet
import urllib2

print ('Start...')
html_1 = urllib2.urlopen('http://www.baidu.com/',timeout=120).read()
print html_1