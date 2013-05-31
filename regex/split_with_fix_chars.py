import re 
A = open('mac.txt','r') 
a = A.readlines() 
for aa in a: 
    b=re.findall(r'.{2}',aa) 
    c='-'.join(b) 
    print c 
A.close() 