from decimal import Decimal

x = Decimal(input())
a = int(x)
b = int(100 * (x - a))
print(a, b)
