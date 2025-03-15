# 1026
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True) # 큰 순서대로 정렬
b.sort()

t = 0
for i in range(n):
    t += a[i] * b[i] # 각각 곱해서 더해주기
    
print(t) # 최솟값
