D = {'food':'Spam','quantity':4,'color':'pink'}
print(D)
print(D.get('food'))
print(D['food'])

D['quantity'] += 1
print(D['quantity'])

print('=' * 50)
D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D)
print(D['name'])

print('=' * 50)
rec = {'name':{'first':'Bob', 'last' : 'Smith'},
	'job':['dev','mgr'],
	'age':40.5
}
print(rec['name'])
print(rec['name']['last'])
print(rec['job'])
print(rec['job'][-1])
rec['job'].append('janitor')
print(rec)

print('=' * 50)
D = {'a' : 1, 'b' : 2, 'c' : 3}
print(D)
Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)
for key in Ks:
	print(key, '=>', D[key])
	print('%s=%s' %(key,D[key]))

for key in sorted(D):
	print('%s=%s'%(key,D[key]))

print('=' * 50)
D = {'a': 1,'c': 3, 'b': 2}
D['e'] = 99
print(D['e'])
if not 'f' in D:
	print('not foudn \'f\'')
else:
	print(D['f'])
value = D.get('x',0)
print value
