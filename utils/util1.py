#!/usr/bin/python  
# -*- coding: utf-8 -*-  
# 通用功能类封装  
import os,time,sys,string,urllib,httplib,shutil,platform,tarfile  
from commands import getstatusoutput as getso  
from ConfigParser import *  
   
def wr_log(str_cmd, status=0, result=""):  
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S")  
    if status == 0:  
        fp = open("log.txt",'a+')  
        fp.write("[%s]\t%s\tdone!\n" % (cur_time, str_cmd))  
        fp.close()  
    else:  
        fp = open("err_log.txt",'a+')  
        fp.write("[%s]\t%s\tfailed!\n%s\n\n" % (cur_time, str_cmd, result))  
        fp.close()  
        sys.exit(-1)  

def wget(url, new_name=""):  
    '''''  
    wget封装，需提供下载地址，新文件名参数可省略。  
       
    例子：  
    wget("http://208.asktao.com/test.txt", "/tmp/test.txt")  
    ''' 
    try:  
        file_name = url[url.rfind("/")+1:]  
        if new_name == "":  
            new_name = file_name  
        fp = urllib.urlopen(url)  
        py_ver = sys.version[:3]  
        if py_ver == "2.4":  
            domain = url.split("/")[2]  
            get_file = "/" + "/".join(url.split("/")[3:])  
            conn = httplib.HTTPConnection(domain)  
            conn.request('GET', get_file)  
            fp_code = conn.getresponse().status  
        else:  
            fp_code = fp.getcode()  
        if fp_code != 200:  
            raise NameError, '%s not exist.'%file_name  
        buf_len = 2048 
        f = open(new_name, 'wb')  
        size = 0 
        while 1:  
            s = fp.read(buf_len)  
            if not s:  
                break 
            f.write(s)  
            size += len(s)  
        fp.close()  
        f.close()  
        wr_log("wget %s"%url)  
    except Exception, e:  
        wr_log("wget %s"%url, 1, e)  
   
def sed(type, file_name, s_str="", d_str=""):  
    '''''  
    sed封装，根据传入的type参数执行相应操作，type可以为以下几种：  
    a  在s_str行后面追加d_str，若s_str为空，则默认在文件尾部追加；  
    i  在s_str行前面插入d_str，若s_str为空，则默认在文件头部插入；  
    d  删除s_str所在行；  
    s  将s_str替换为d_str。  
       
    type及file_name为必需的参数。  
       
    例子：  
    替换字符串：sed("s", "/etc/test.txt", "abc", "123")  
    ''' 
    try:  
        fp = open(file_name)  
        cont = fp.read()  
        fp.close()  
        content = cont.split("\n")  
        content2 = cont.split("\n")  
        cnt = 0 
        idx = 0 
        if type == "a":  
            str_cmd = "sed -i '/%s/a %s' %s" % (s_str, d_str, file_name)  
            if not s_str:  
                content.append(d_str)  
            else:  
                for i in content2:  
                    if i.find(s_str) != -1:  
                        x = idx + 1 + cnt  
                        content.insert(x, d_str)  
                        cnt += 1 
                    idx += 1 
        elif type == "i":  
            str_cmd = "sed -i '/%s/i %s' %s" % (s_str, d_str, file_name)  
            if not s_str:  
                content.insert(0, d_str)  
            else:  
                for i in content2:  
                    if i.find(s_str) != -1:  
                        x = idx + cnt  
                        content.insert(x, d_str)  
                        cnt += 1 
                    idx += 1 
        elif type == "d":  
            str_cmd = "sed -i '/%s/d' %s" % (s_str, file_name)  
            for i in content2:  
                if i.find(s_str) != -1:  
                    idx = content.remove(i)  
        elif type == "s":  
            str_cmd = "sed -i 's/%s/%s/g' %s" % (s_str, d_str, file_name)  
            cont = string.replace(cont, s_str, d_str)  
            content = cont.split("\n")  
        fp = open(file_name, "w")  
        fp.write("\n".join(content))  
        fp.close()  
        wr_log(str_cmd)  
    except Exception, e:  
        wr_log("modify %s" % file_name, 1, e)  
   
def md(dir_name):  
    '''''  
    mkdir封装，创建传入的目录名称。  
    ''' 
    try:  
        if not os.path.exists(dir_name):  
            os.makedirs(dir_name)  
            wr_log("mkdir %s"%dir_name)  
        else:  
            wr_log("%s is exist."%dir_name)  
    except Exception, e:  
        wr_log("mkdir %s"%dir_name, 1, e)  
   
def mv(src, dst):  
    '''''  
    mv封装，移动文件或修改文件名。  
    ''' 
    try:  
        try:  
            os.rename(src, dst)  
        except OSError:  
            if os.path.dirname(src) == dst or os.path.dirname(src) == os.path.dirname(dst):  
                raise Exception, "Cannot move self." 
            if os.path.isdir(src):  
                if os.path.abspath(dst).startswith(os.path.abspath(src)):  
                    raise Exception, "Cannot move a directory to itself." 
                _copy(src, dst)  
                shutil.rmtree(src)  
            else:  
                shutil.copy2(src,dst)  
                os.unlink(src)  
        wr_log("mv %s %s"%(src, dst))  
    except Exception, e:  
        wr_log("mv %s %s"%(src, dst), 1, e)  
   
def cp(src, dst):  
    '''''  
    cp封装，复制文件或目录。  
    ''' 
    try:  
        _copy(src, dst)  
        wr_log("cp %s %s"%(src, dst))  
    except Exception, e:  
        wr_log("cp %s %s"%(src, dst), 1, e)  
   
def _copy(src, dst):  
    '''''  
    copy封装，供cp调用。  
    ''' 
    if os.path.isdir(src):  
        base = os.path.basename(src)  
        if os.path.exists(dst):  
            dst = os.path.join(dst, base)  
        if not os.path.exists(dst):  
            os.makedirs(dst)  
        names = os.listdir(src)  
        for name in names:  
            srcname = os.path.join(src, name)  
            _copy(srcname, dst)  
    else:  
        shutil.copy2(src, dst)  
   
def touch(src):  
    '''''  
    linux适用  
       
    touch封装，新建空白文件。  
    ''' 
    str_cmd = "/bin/touch %s" % src  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
   
def rm(src):  
    '''''  
    rm封装，删除文件或目录，非交互式操作，请谨慎操作。  
    ''' 
    try:  
        if os.path.exists(src):  
            if os.path.isfile(src):  
                os.remove(src)  
            elif os.path.isdir(src):  
                shutil.rmtree(src)  
            wr_log("rm %s" % src)  
    except Exception, e:  
        wr_log("rm %s" % src, 1, e)  
   
def chmod(num, file_name):  
    '''''  
    linux适用  
       
    chmod封装，修改文件权限。  
    需要传入一个八进制数以及文件名。  
       
    例子：  
    chmod(644, "/tmp/test.txt")  
    ''' 
    str_cmd = "/bin/chmod %s %s" % (num, file_name)  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
   
def chown(user, file_name, arg=""):  
    '''''  
    linux适用  
       
    chown封装，修改文件属主属组。  
       
    例子：  
    chown("nobody.nobody", "/tmp", "r")  
    ''' 
    if arg == "r":  
        str_cmd = "/bin/chown -R %s %s" % (user, file_name)  
    else:  
        str_cmd = "/bin/chown %s %s" % (user, file_name)  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
   
def rar(dst,src):  
    '''''  
    windows适用  
       
    winrar 压缩文件  如： rar(c:\dat.rar c:\dat)  
    ''' 
    try:  
        if not os.path.exists(src) or not os.path.exists(os.path.dirname(dst)):  
            raise Exception, "%s or %s not exist!" % (src, os.path.dirname(dst))  
        os.system(r'C:\Progra~1\WinRAR\rar a %s %s' % (dst,src))  
        wr_log("rar %s to %s" % (src, dst))  
    except Exception,e:  
        wr_log("rar %s to %s" % (src, dst), 1, e)  
   
def unrar(src,dst):  
    '''''  
    windows适用  
       
    unrar 解压缩rar文件 到目标路径 如：unrar(c:\dat.rar c:\)  
    ''' 
    try:  
        if not os.path.exists(dst) or not os.path.exists(src):  
            raise Exception, "%s or %s not exist!" % (src, dst)  
        os.system(r'C:\Progra~1\WinRAR\rar x %s %s' % (src, dst))  
        wr_log("unrar %s" % src)  
    except Exception,e:  
        wr_log("unrar %s" % src, 1, e)  
   
def tar(dst, src):  
    '''''  
    linux适用  
       
    tar封装，压缩文件。  
       
    例子：  
    tar("/tmp/test.tgz", "/tmp/test.txt")  
    ''' 
    str_cmd = "/bin/tar zcf %s %s" % (dst, src)  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
       
def untgz(tgz_file, dst="./"):  
    '''''  
    tar封装，解压缩文件。  
       
    例子：  
    untgz("/tmp/test.tgz", "/tmp")  
    ''' 
    try:  
        tarobj = tarfile.open(tgz_file)  
        names = tarobj.getnames()  
        for name in names:  
            tarobj.extract(name,path=dst)  
        tarobj.close()  
        wr_log("untgz %s" % tgz_file)  
    except Exception, e:  
        wr_log("untgz %s" % tgz_file, 1, e)  
       
def kill(arg):  
    '''''  
    linux中，查找进程并杀死返回的pid。  
    windows中，查找进程或端口并杀死返回的pid。  
    ''' 
    pid = get_pid(arg)  
    os_type = platform.system()  
    if os_type == "Linux":  
        if pid:  
            str_cmd = "/bin/kill -9 %s" % pid  
            status, result = getso(str_cmd)  
            wr_log("kill %s" % arg, status, result)  
    elif os_type == "Windows":  
        if pid:  
            try:  
                import ctypes  
                for i in pid:  
                    handle = ctypes.windll.kernel32.OpenProcess(1, False, i)  
                    ctypes.windll.kernel32.TerminateProcess(handle,0)  
                wr_log("kill %s" % arg)  
            except Exception, e:  
                wr_log("kill %s" % arg, 1, e)  
   
def get_pid(arg):  
    '''''  
    linux中，查找进程并返回pid。  
    windows中，查找进程或端口返回pid。  
    ''' 
    os_type = platform.system()  
    if os_type == "Linux":  
        str_cmd = "/bin/ps auxww | grep '%s' | grep -v grep | awk '{print $2}'" % arg  
        status, result = getso(str_cmd)  
        return result  
    elif os_type == "Windows":  
        if type(arg) == int:  
            str_cmd =  "netstat -ano|find \"%s\""%arg  
            try:  
                result = os.popen(str_cmd,"r").read()  
                result = result.split("\n")[0].strip()  
                if result.find("WAIT") != -1:  
                    return 0 
                pid = int(result[result.rfind(" "):].strip())  
                return [pid]  
            except Exception, e:  
                return 0 
        else:  
            import win32con,win32api,win32process  
            pids = []  
            for pid in win32process.EnumProcesses():  
                try:  
                    hProcess = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)  
                    hProcessFirstModule = win32process.EnumProcessModules(hProcess)[0]  
                    processName = os.path.splitext(os.path.split(win32process.GetModuleFileNameEx(hProcess, hProcessFirstModule))[1])[0]  
                    if processName == arg:  
                        pids.append(pid)  
                except Exception, e:  
                    pass 
            return pids  
   
def grpadd(grp_name):  
    '''''  
    linux适用  
       
    groupadd封装，增加组。  
    ''' 
    str_cmd = "/usr/sbin/groupadd %s" % grp_name  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
   
def useradd(user_name, arg=""):  
    '''''  
    useradd封装，添加新用户；  
    linux和windows系统分别使用不同方法；  
    在linux中，arg填写新用户的gid；  
    windows中，arg填写新用户的密码。  
    ''' 
    os_type = platform.system()  
    if os_type == "Linux":  
        str_cmd = "/usr/bin/id %s" % user_name  
        status, result = getso(str_cmd)  
        if status == 0:  
            return 
        if not arg:  
            str_cmd = "/usr/sbin/useradd %s" % user_name  
        else:  
            str_cmd = "/usr/sbin/useradd -g %s %s" % (arg, user_name)  
        status, result = getso(str_cmd)  
        wr_log(str_cmd, status, result)  
    elif os_type == "Windows":  
        try:  
            import win32netcon,win32net,wmi  
            for use in wmi.WMI().Win32_UserAccount():  
                if use.name == user_name:  
                    raise Exception, "user %s is already exists" % user_name  
            udata = {}  
            udata["name"] = user_name  
            udata["password"] = arg  
            udata["flags"] = win32netcon.UF_NORMAL_ACCOUNT | win32netcon.UF_SCRIPT  
            udata["priv"] = win32netcon.USER_PRIV_USER  
            win32net.NetUserAdd(None, 1, udata)  
            wr_log("add user %s" % user_name)  
        except Exception,e:  
            wr_log("add user %s" % user_name, 1, e)  
   
def userdel(user_name):  
    '''''  
    userdel封装，删除用户。  
    ''' 
    os_type = platform.system()  
    if os_type == "Linux":  
        str_cmd = "/usr/bin/id %s" % user_name  
        status, result = getso(str_cmd)  
        if status == 0:  
            str_cmd = "/usr/sbin/userdel -r %s" % user_name  
            status, result = getso(str_cmd)  
            wr_log(str_cmd, status, result)  
    elif os_type == "Windows":  
        try:  
            import win32net,wmi  
            for use in wmi.WMI().Win32_UserAccount():  
                if use.name == user_name:  
                    win32net.NetUserDel(None,user_name)  
                    wr_log("del user %s" % user_name)  
                    return 
            wr_log("user %s not exists" % user_name)  
        except Exception,e:  
            wr_log("del user %s" % user_name, 1, e) 

def main():
    # wr_log('test hello')
    print("starting to download...")
    wget("http://www.tutorialspoint.com/jsf/jsf_tutorial.pdf","1.pdf")
    print("finished download...")
'''
starting to download...
finished download...
[Finished in 195.0s]
'''

if __name__ == '__main__':
    main()        