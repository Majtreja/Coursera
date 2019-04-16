k = int(input())
ans = 0

for i in range(1, k + 1):
    if str(i) == str(i)[::-1]:
        ans += 1
print(ans)
