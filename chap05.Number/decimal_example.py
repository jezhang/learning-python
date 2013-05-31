import decimal
from decimal import Decimal

print(0.1 + 0.1 + 0.1 - 0.3)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print('=' * 50)

print(Decimal(1) / Decimal(7))
decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print('='*50)
print(1999 + 1.33)
decimal.getcontext().prec = 2
pay = Decimal(str(1999 + 1.33))
print(pay)
print('=' * 50)
