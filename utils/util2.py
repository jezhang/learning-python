#!/usr/bin/python  
# -*- coding: utf-8 -*-  
# 通用功能类封装  
import os,time,sys,string,urllib,httplib,shutil,platform,tarfile  
from commands import getstatusoutput as getso  
from ConfigParser import *  
 
def hostname(host_name):  
    '''''  
    linux适用  
       
    hostname封装，修改主机名。  
    ''' 
    str_cmd = "/bin/sed -i 's/HOSTNAME/#&/;$a HOSTNAME=%s' /etc/sysconfig/network;/bin/hostname %s" % (host_name,host_name)  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
   
def md5sum(file_name):  
    '''''  
    md5sum封装，获取文件的md5值  
    ''' 
    if os.path.isfile(file_name):  
        f = open(file_name,'rb')  
        py_ver = sys.version[:3]  
        if py_ver == "2.4":  
            import md5 as hashlib  
        else:  
            import hashlib  
            md5 = hashlib.md5(f.read()).hexdigest()  
            f.close()  
            return md5  
    else:  
        return 0 
   
def md5(file_name):  
    '''''  
    linux适用  
   
    md5sum -c 封装，校验md5文件，返回校验成功或失败状态  
    ''' 
    str_cmd="/usr/bin/md5sum -c %s" % file_name  
    status,result=getso(str_cmd)  
    return status  
   
def grep(s_str, file_name):  
    '''''  
    grep封装，查找文件中关键字，有则返回所在行，否则返回空字符串。  
    ''' 
    try:  
        fd = open(file_name)  
        content = fd.read()  
        result = ""  
        if content.find(s_str) != -1:  
            for line in content.split("\n"):  
                if line.find(s_str) != -1:  
                    result = result + line + "\n" 
        return result.strip()  
    except Exception, e:  
        wr_log("grep %s %s" % (s_str, file_nsme), 1, e)  
   
def rwconf(type, file_name, section, option, s_str=""):  
    '''''  
    读取标准的ini格式配置文件，type可为以下值：  
    get     获取section下的option的值，值为字符串；  
    getint  获取section下的option的值，值为数字；  
    modi    修改section下的option的值，并保存；  
    del     删除section下的option，并保存。  
   
    注：option严格区分大小写  
    ''' 
    try:  
        if type == "get" or type == "getint":  
            cf = ConfigParser()  
        else:  
            cf = ConfParser()  
        cf.read(file_name)  
        if type == "get":  
            return cf.get(section, option)  
        elif type == "getint":  
            return cf.getint(section, option)  
        elif type == "modi":  
            try:  
                cf.set(section, option, s_str)  
                cf.write(open(file_name, "w"))  
                wr_log("modify %s for %s" % (option, file_name))  
            except Exception, e:  
                wr_log("modify %s for %s" % (option, file_name), 1, str(e))  
        elif type == "del":  
            try:  
                cf.remove_option(section, option)  
                cf.write(open(file_name, "w"))  
                wr_log("del %s for %s" % (option, file_name))  
            except Exception, e:  
                wr_log("del %s for %s" % (option, file_name), 1, str(e))  
    except Exception, e:  
        wr_log("read %s for %s" % (option, file_name), 1, str(e))  
   
def chkconfig(type, svr_name, switch=""):  
    '''''  
    linux适用  
       
    chkconfig封装，根据传入的type参数执行相应操作，type可以为以下几种：  
    add  添加服务至启动项；  
    del  从启动项删除服务；  
    数字  指定运行级别的服务开启或关闭。  
       
    type及svr_name为必需的参数。  
       
    例子：  
    开启运行级别3的sshd服务：chkconfig("3", "sshd", "on")  
    ''' 
    if type != "add" and type != "del":  
        type = "--level %s" % str(type)  
    str_cmd = "/sbin/chkconfig %s %s %s" % (type, svr_name, switch)  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
   
def passwd(user_name,newpass):  
    '''''  
    passwd封装，修改用户密码  
    ''' 
    os_type = platform.system()  
    if os_type == "Linux":  
        str_cmd = "echo '%s' | passwd %s --stdin" % (newpass, user_name)  
        status, result = getso(str_cmd)  
        wr_log(str_cmd, status, result)  
    elif os_type == "Windows":  
        try:  
            if os.system('net user %s "%s" ' %(user_name,newpass)) == 0:  
                wr_log("modify passwd for %s  " % user_name)  
            elif os.system('net user %s "%s" ' %(user_name,newpass)) == 2:  
                raise Exception, "user %s isnot exists" % user_name  
        except Exception,e:  
            wr_log("modify passwd for %s " % user_name, 1, e)  
   
def echo(str, file_name):  
    '''''  
    linux适用  
   
    echo封装，添加字符串到文件尾部  
    ''' 
    str_cmd = "/bin/echo '%s' >> %s" % (str, file_name)  
    status, result = getso(str_cmd)  
    wr_log(str_cmd, status, result)  
   
def upload(localfiles, remotepath, host="xxx", username="xxx", password="xxxx"):  
    '''''  
    上传文件至ftp服务器，默认上传至208FTP，如要上传至其它FTP服务器，请指定host/user/pass  
   
    例：  
    upload("a.txt,b.txt", "/test/")  
    上传a.txt、b.txt文件到208的test目录下  
    ''' 
    import base64  
    from ftplib import FTP  
    try:  
        localfiles = localfiles.split(",")  
        f =FTP(host)  
        f.login(username,password)  
        f.cwd(remotepath)  
        for localfile in localfiles:  
            fd = open(localfile,'rb')  
            f.storbinary('STOR %s' % os.path.basename(localfile),fd)  
            fd.close()  
        f.quit()  
        wr_log("upload %s" % localfiles)  
    except Exception, e:  
        wr_log("upload %s" % localfiles, 1, e)  
   
class ConfParser(RawConfigParser):  
    '''''  
    ConfigParser模块有一个缺陷,改写ini文件的某个section的某个option,写入ini文件后  
    ini文件的注释都丢掉了,并且option的大写字母都转换成了小写  
    为了保存ini文件的注释以及option的大小写，重写了write、set、optionxform等方法，由rwconf函数调用  
    ''' 
    def write(self, fp):  
        """Write an .ini-format representation of the configuration state.  
   
        write ini by line no  
        """ 
           
        if self._defaults:  
            section = DEFAULTSECT  
            lineno = self._location[section]  
            self._data[lineno] = "[%s]\n" %section  
            for (key, value) in self._defaults.items():  
                if key != "__name__":  
                    wholename = section + '_' + key  #KVS  
                    lineno = self._location[wholename]  
                    self._data[lineno] = "%s = %s\n" %(key, str(value).replace('\n', '\n\t'))  
                       
        for section in self._sections:  
            lineno = self._location[section]  
            self._data[lineno] = "[%s]\n" % section  
            for (key, value) in self._sections[section].items():  
                if key != "__name__":  
                    wholename = section + '_' + key  #KVS  
                    lineno = self._location[wholename]  
                    self._data[lineno] = "%s = %s\n" %(key, str(value).replace('\n', '\n\t'))  
               
        for line in self._data:  
            fp.write("%s"%line)  
        fp.close()  
               
    def _read(self, fp, fpname):  
        """Parse a sectioned setup file.  
   
        When parsing ini file, store the line no in self._location  
        and store all lines in self._data  
        """ 
        self._location = {}  
        self._data = []  
        cursect = None      # None, or a dictionary  
        optname = None 
        lineno = 0 
        e = None            # None, or an exception  
        while True:  
            line = fp.readline()  
            self._data.append(line) #KVS  
            if not line:  
                break 
            lineno = lineno + 1 
            if line.strip() == '' or line[0] in '#;':  
                continue 
            if line.split(None, 1)[0].lower() == 'rem' and line[0] in "rR":  
                # no leading whitespace  
                continue 
            if line[0].isspace() and cursect is not None and optname:  
                value = line.strip()  
                if value:  
                    cursect[optname] = "%s\n%s" % (cursect[optname], value)  
            else:  
                mo = self.SECTCRE.match(line)  
                if mo:  
                    sectname = mo.group('header')  
                    if sectname in self._sections:  
                        cursect = self._sections[sectname]  
                    elif sectname == DEFAULTSECT:  
                        cursect = self._defaults  
                        self._location[DEFAULTSECT] = lineno -1 #KVS  
                           
                    else:  
                        cursect = {'__name__': sectname}  
                        self._location[sectname] = lineno -1 #KVS  
                        self._sections[sectname] = cursect  
   
                    optname = None 
                elif cursect is None:  
                    raise MissingSectionHeaderError(fpname, lineno, line)  
                else:  
                    mo = self.OPTCRE.match(line)  
                    if mo:  
                        optname, vi, optval = mo.group('option', 'vi', 'value')  
                        if vi in ('=', ':') and ';' in optval:  
                            pos = optval.find(';')  
                            if pos != -1 and optval[pos-1].isspace():  
                                optval = optval[:pos]  
                        optval = optval.strip()  
                        if optval == '""':  
                            optval = '' 
                        optname = self.optionxform(optname.rstrip())  
                        cursect[optname] = optval  
                           
                        if cursect == self._defaults:  
                            wholename = DEFAULTSECT + '_' + optname  #KVS  
                        else:  
                            wholename = cursect['__name__'] + '_' + optname  #KVS  
                        self._location[wholename] = lineno-1     #KVS  
                    else:  
                        if not e:  
                            e = ParsingError(fpname)  
                        e.append(lineno, repr(line))  
        if e:  
            raise e  
   
    def add_section(self, section):  
        """Create a new section in the configuration.  
   
        Raise DuplicateSectionError if a section by the specified name  
        already exists.  
        """ 
        if section in self._sections:  
            raise DuplicateSectionError(section)  
        self._sections[section] = {}  
   
        linecount = len(self._data)  
        self._data.append('\n')  
        self._data.append('%s'%section)  
        self._location[section] = linecount + 1 
   
    def set(self, section, option, value):  
        """Set an option.""" 
        if not section or section == DEFAULTSECT:  
            sectdict = self._defaults  
        else:  
            try:  
                sectdict = self._sections[section]  
            except KeyError:  
                raise NoSectionError(section)  
        option = self.optionxform(option)  
        add = False 
        if not option in sectdict:  
            add = True 
        sectdict[self.optionxform(option)] = value  
        if add:  
            lineno = self._location[section]  
            self._data.append('')  
            idx = len(self._data)  
            while idx>lineno:  
                self._data[idx-1] = self._data[idx-2]  
                idx = idx-1 
            self._data[idx+1] = '%s = %s\n'%(option,value)  
            self._location[section+'_'+option]=idx+1 
            for key in self._location:  
                if self._location[key] > lineno:  
                    self._location[key] = self._location[key] + 1 
            self._data[idx+1] = '%s = %s\n'%(option,value)  
            self._location[section+'_'+option]=idx+1 
   
    def remove_option(self, section, option):  
        """Remove an option. """ 
        if not section or section == DEFAULTSECT:  
            sectdict = self._defaults  
        else:  
            try:  
                sectdict = self._sections[section]  
            except KeyError:  
                raise NoSectionError(section)  
        option = self.optionxform(option)  
        existed = option in sectdict  
        if existed:  
            del sectdict[option]  
            wholename = section + '_' + option  
            lineno  = self._location[wholename]  
               
            del self._location[wholename]  
            for key in self._location:  
                if self._location[key] > lineno:  
                    self._location[key] = self._location[key] -1 
            del self._data[lineno]  
        return existed  
   
    def remove_section(self, section):  
        """Remove a file section.""" 
        existed = section in self._sections  
        if existed:  
            lstOpts = []  
            for option in self._sections[section]:  
                if option == '__name__':  
                    continue 
                lstOpts.append(option)  
            for option in lstOpts:  
                self.remove_option(section,option)  
   
            del self._sections[section]  
            wholename = section  
            lineno  = self._location[wholename]  
               
            del self._location[wholename]  
            for key in self._location:  
                if self._location[key] > lineno:  
                    self._location[key] = self._location[key] -1 
            del self._data[lineno]  
        return existed  
   
    def optionxform(self, optionstr):  
        ''''' 防止大小写转换''' 
        return optionstr 