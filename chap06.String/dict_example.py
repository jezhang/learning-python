from datetime import datetime

f = open('template_dict.txt')
s = f.read()
f.close()
# ss = s.format('Jean Zhang','1984', 'SSC')
values = {'name' : 'Jean', 'age':20}
d = datetime.now()
f = open(d.strftime('%Y%m%d%H%M%S%Z') + '.txt','w')
f.write(s % values)
f.close()