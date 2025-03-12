n = int(input())

li = list(map(int, input().split()))

li.sort()

min = 0
for i in range(1, n+1):
    min += sum(li[0:i])

print(min)