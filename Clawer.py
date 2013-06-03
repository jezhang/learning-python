#!/usr/bin/env python
#-*- coding:utf-8 -*-
# from BeautifulSoup import BeautifulSoup
from Queue import Queue
# from mechanize import Browser
import urllib2, mechanize, re

class Clawer(object):
    def __init__(self, username, password):
        self.br = Browser()
        self.username = username
        self.password = password
        self.queue = Queue()
        self.urls = {}
    def login(self, url):
        self.br.open(url)
        self.br.select_form(nr = 0)
        self.br['email'] = self.username
        self.br['password'] = self.password
        resp = self.br.submit()
        self.queue.put(resp.geturl())
 
    def run(self):
        self.login("http://www.renren.com/GLogin.do")
        while not self.queue.empty():
            match1 = re.compile('(portal=)|(pma=)|(profile.do?id=)') 
            match2 = re.compile('username.*')
            match3 = re.compile('userpic')

            url  = self.queue.get()
            try:
                resp = self.br.open(url)
            except Exception, e:
                print e
                url = self.queue.get()
                self.login("http://www.renren.com/GLogin.do")
                resp = self.br.open(url)
            page = resp.read()
            soup = BeautifulSoup(page)
            resp1 = soup.findAll('a', attrs = {'href': match1})
            resp2 = soup.findAll('h1', attrs = {'class': match2})
            resp3 = soup.findAll('img', attrs = {'id': match3}) 
             
            for a in resp1:
                if not self.urls.has_key(a['href']):
                    self.urls[a['href']]  = 1
                    self.queue.put(a['href'])
            if resp2 and resp3:
                if resp2[0].text and resp3[0]['src']:
                    name = resp2[0].text
                    url_img = resp3[0]['src']
                else:
                    continue
            else:
                continue
           
            try:
                img = urllib2.urlopen(url_img)
            except:
                print 'img can not open:', url_img
                continue
            try:
                data = img.read()
            except:
                print 'img can not read:', url_img
                continue
            try:
                fp = open(name, 'w')
                fp.write(data)
                fp.close()
                print 'download:', name
            except:
                print 'img can not write:', url_img
 
if __name__ == "__main__":
    clawer = Clawer('jean.zhang.cn@gmail.com', 'welcome')
    clawer.run()