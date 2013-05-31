from fractions import Fraction

x = Fraction(1,3)
print(x)

y = Fraction(4,6)
print(y)

print(x + y)
print(x - y)
print(x * y)

print('='*50)
print(Fraction('0.25'))
print(Fraction('1.25'))
print(Fraction('0.25') + Fraction('1.25'))

print('='*50)
a = 1 / 3.0
b = 4 / 6.0
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)

print('='*50)
print(0.1 + 0.1 + 0.1 - 0.3)
print(Fraction(1,10) + Fraction(1,10) + Fraction(1,10) - Fraction(3,10))

print('='*50)
print((2.5).as_integer_ratio())
print((0.25).as_integer_ratio())
f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)
