#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
 
import os 
import os.path 
import shutil 
import time,datetime 
 
def copyFiles(sourceDir,  targetDir): #把某一目录下的所有文件复制到指定目录中 
     if sourceDir.find(".svn") > 0: 
         return 
     for file in os.listdir(sourceDir): 
         sourceFile = os.path.join(sourceDir,  file) 
         targetFile = os.path.join(targetDir,  file) 
         if os.path.isfile(sourceFile): 
             if not os.path.exists(targetDir): 
                 os.makedirs(targetDir) 
             if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))): 
                     open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
         if os.path.isdir(sourceFile): 
             First_Directory = False 
             copyFiles(sourceFile, targetFile) 
 
def removeFileInFirstDir(targetDir):#删除一级目录下的所有文件 
    for file in os.listdir(targetDir): 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(targetFile): 
            os.remove(targetFile) 
 
def coverFiles(sourceDir,  targetDir):#复制一级目录下的所有文件到指定目录 
         for file in os.listdir(sourceDir): 
             sourceFile = os.path.join(sourceDir,  file) 
             targetFile = os.path.join(targetDir,  file) 
             #cover the files 
             if os.path.isfile(sourceFile): 
                 open(targetFile,"wb").write(open(sourceFile,"rb").read()) 
 
def moveFileto(sourceDir,  targetDir):#复制指定文件到目录 
    shutil.copy(sourceDir,  targetDir) 
 
def writeVersionInfo(targetDir):#往指定目录写文本文件 
    open(targetDir, "wb").write("Revison:") 
 
def getCurTime():#返回当前的日期，以便在创建指定目录的时候用 
     nowTime = time.localtime() 
     year = str(nowTime.tm_year) 
     month = str(nowTime.tm_mon) 
     if len(month) < 2: 
         month = '0' + month 
     day =  str(nowTime.tm_yday) 
     if len(day) < 2: 
         day = '0' + day 
     return (year + '-' + month + '-' + day) 
 
if  __name__ =="__main__":#主函数 
     print "Start(S) or Quilt(Q) \n" 
     flag = True 
     while (flag): 
         answer = raw_input() 
         if  answer == 'Q': 
             flag = False 
         elif answer == 'S': 
             formatTime = getCurTime() 
             targetFoldername = "Build " + formatTime + "-01" 
             Target_File_Path += targetFoldername 
             copyFiles(Debug_File_Path,   Target_File_Path) 
             removeFileInFirstDir(Target_File_Path) 
             coverFiles(Release_File_Path,  Target_File_Path) 
             moveFileto(Firebird_File_Path,  Target_File_Path) 
             moveFileto(AssistantGui_File_Path,  Target_File_Path) 
             writeVersionInfo(Target_File_Path+"\test.txt") 
             print "all sucess" 
         else: 
             print "not the correct command" 