X = set('spam')
# Y = {'h','a','m'}   Make a set with new 3.0 set literals

print(sorted(X))
X.add('s')
print(X)

print('='*50)

print(1.0/3)
print((2.0/3) + (1.0/2))

import decimal
d = decimal.Decimal('3.141')
print(d + 1)
print(type(d))

print(decimal.getcontext().prec)
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


