from datetime import datetime

f = open('template_replace.txt')
s = f.read()
f.close()
# ss = s.format('Jean Zhang','1984', 'SSC')
s = s.replace('{name}','Jean Zhang')
s = s.replace('{birthyear}','1984')
s = s.replace('{cosmpany}','SSC')
d = datetime.now()
f = open(d.strftime('%Y%m%d%H%M%S%Z') + '.txt','w')
f.write(s)
f.close()