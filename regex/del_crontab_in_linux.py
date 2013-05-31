#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
 
import time 
 
def del_cront(): 
    f = '/var/spool/cron/apache' 
    read = open(f,'r') 
    cront = read.readlines()#读取apache用户cron文件的内容 
    read = open(f,'w') 
    read.write("")#清除当前文件的内容 
    for line in cront: 
        if '#' not in line: 
            a = ' '.join(line.strip().split()[0:4])#截取cron中的月、日、时、分字段 
            aa = str(time.localtime()[0]) + ':' + ':'.join(a.split()[::-1]) + ':00'#格式化截取到的时间字段为%Y:%m:%d:%H:%M:%S格式 
            cront_time = time.mktime(time.strptime(aa, '%Y:%m:%d:%H:%M:%S'))#标准时间格式转化为时间戳 
            print a,aa,cront_time 
            now = time.time()#当前的时间的时间戳 
            if now < cront_time: 
                read.write(line)#大于当前时间的任务回写到cron文件中，保留 
        else: 
            read.write(line)#注释之类的保留到文件中 
    read.close 
 
if __name__=="__main__": 
    del_cront() 