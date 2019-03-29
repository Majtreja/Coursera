prev = int(input())
answer = 0
while prev != 0:
    n = int(input())
    if n != 0 and prev < n:
        answer += 1
    prev = n
print(answer)
