p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1

money_before = 100 * x + y
money_after = int(money_before * (100 + p) / 100)
itog = 0

while i < k:
    itog = int(money_after + (p * money_after) / 100)
    money_after = itog
    i += 1

print(itog // 100, itog % 100)
