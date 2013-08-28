#虽然版本控制系统更强大，但这个脚本在开发工作中然后很有用。我常常对它进行定制，比如只对某个特定后缀名的文件进行备份；在for file in files 循环的内部加一个适当的测试就行了。如：name, ext = os.path.splitext(file) if ext not in  ('.py', '.txt', '.doc'):continue 代码片段首先使用标准库模块os.path的splitext函数来获得文件的扩展名（以一个句号开始），放入局部变量ext中，然后，如果文件拓展名不是我们感兴趣的几个扩展名之一，我们就执行continue语句，进入下一轮循环。

import sys, os, shutil, filecmp
MAXVERSIONS = 100
def backup(tree_top, bakdir_name = 'bakdir'):
    for dir, subdirs, files in os.walk(tree_top):
        #make sure each dir has subdir called bakdir
        backup_dir = os.path.join(dir, bakdir_name)
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        #stop recurse the backup dir
        subdirs[:] = [ d for d in subdirs if d != bakdir_name ]
        for file in files:
            filepath = os.path.join(dir,file)
            destpath = os.path.join(backup_dir, file)
        #check if the old version exist
            for index in xrange(MAXVERSIONS):
                backup = '%s.%2.2d' % (destpath, index)
                if not os.path.exists(backup):
                    break
            if index > 0:
            #there is no need to backup if the file is the same as the new version
                old_backup = '%s.%2.2d' %(destpath, index-1)
                abspath = os.path.abspath(filepath)
                try:
                    if os.path.isfile(old_backup) and filecmp.cmp(abspath, old_backup,shallow = False):
                        continue
                except OSError:
                    pass
            try:
                shutil.copy(filepath, backup)
            except OSError:
                pass

if __name__ == '__main__':
    #backup dir
    try:
        tree_top = 'd:\\adb'#sys.argv[1]
    except IndexError:
        tree_top = '.'
    backup(tree_top)
