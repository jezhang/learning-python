#coding:utf-8

with open('a.ini') as f1:
	list1 = f1.readlines()

for item in list1:
	__import__(item.strip())