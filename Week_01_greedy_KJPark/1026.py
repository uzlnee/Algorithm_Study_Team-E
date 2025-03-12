# 1 - 둘 다 리스트를 정렬하고 푸는 방법
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# S의 최솟값을 출력하는 방법: 리스트 a, b를 각각 오름, 내림 차순으로 정렬해서 서로 곱해준다.
a_list_rev = sorted(a_list, reverse=True)
b_list_sort = sorted(b_list)

total = 0
for i in range(n):
    total += a_list_rev[i] * b_list_sort[i]
    
print(total)


# 2 - 문제의 조건대로, B는 고정하고 A만 재배열하여 푸는 방법
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
total = 0
for i in range(n):
    b_value_max = max(b_list)
    total += a_list[i] * b_value_max
    b_list.remove(b_value_max)
    
print(total)
