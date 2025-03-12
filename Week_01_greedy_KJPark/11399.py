# 첫번째 방법
n = int(input())
sorted_time = sorted(list(map(int, input().split())))
min_total = 0

# sorted_time의 0번 원소는 N번, 1번 원소는 N-1번, 2번 원소는 N-2번...의 식으로 더함
for i in range(n):
    min_total += sorted_time[i] * (n - i)

print(min_total)


# 두번째 방법
n = int(input())
sorted_time = sorted(list(map(int, input().split())))
min_total = 0

# 이중 반복문을 적용하여, 1번사람부터 N번 사람까지 걸리는 시간을 각각 계산하여 더함
for i in range(n):
    current_sum = sum(sorted_time[j] for j in range(i+1))
    min_total += current_sum

print(min_total)
