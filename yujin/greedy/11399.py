N = int(input())
times = list(map(int, input().split()))
times.sort()
waitings = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        waitings[i] = times[i]
    else:
        waitings[i] = waitings[i-1] + times[i]
    
answer = sum(waitings)
print(answer)
