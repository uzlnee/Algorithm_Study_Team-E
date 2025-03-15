# 11399
n = int(input())
l = list(map(int, input().split()))
l.sort() # 리스트의 앞 쪽에 있을 수록 더 많은 횟수가 더해지기 때문에 최솟값을 위해서는 작은 순서대로 정렬

t = 0 # 시간
for i in range(n):
    t += l[i] * (n-i)
print(t)
