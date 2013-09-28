# -*- coding: utf-8 -*-

import urllib2  
  
def get_file_size_by_url(url, proxy=None):  
    """通过content-length头获取文件大小 
    url - 目标文件URL 
    proxy - 代理 
    """  
    opener = urllib2.build_opener()  
    if proxy:  
        if url.lower().startswith('https://'):  
            opener.add_handler(urllib2.ProxyHandler({'https' : proxy}))  
        else:  
            opener.add_handler(urllib2.ProxyHandler({'http' : proxy}))  
    request = urllib2.Request(url)  
    request.get_method = lambda: 'HEAD'  
    try:  
        response = opener.open(request)  
        response.read()  
    except Exception, e:  
        print '%s %s' % (url, e)  
    else:  
        return dict(response.headers).get('content-length', 0)  
  
if __name__ == '__main__':  
    print get_file_size_by_url(url='http://d.hiphotos.baidu.com/album/w%3D2048/sign=fe2dd98d7a899e51788e3d14769fd833/3812b31bb051f8194dcf093adbb44aed2f73e7dc.jpg') 