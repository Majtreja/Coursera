a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2
s = format((p * (p - a) * (p - b) * (p - c))**0.5, '.6')

print(s)
