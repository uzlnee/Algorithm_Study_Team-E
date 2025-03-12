N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0: # N이 5로 나누어 떨어질 때
        cnt += N // 5
        break
    N -= 3 # N이 5로 나누어 떨어지지 않을 때
    cnt += 1

if N < 0:
    print(-1)
else:
    print(cnt)
