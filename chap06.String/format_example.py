from datetime import datetime

f = open('template_format.txt')
s = f.read()
f.close()
ss = s.format('Jean Zhang','1984', 'SSC',name='Austin')
d = datetime.now()
f = open(d.strftime('%Y%m%d%H%M%S%Z') + '.txt','w')
f.write(ss)
f.close()