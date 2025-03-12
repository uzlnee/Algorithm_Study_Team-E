n = int(input())
min_bags = float('inf') # 조합 가능한 경우가 없는 경우, -1 출력을 위한 장치

if n % 5 == 0:
    min_bags = n // 5   # 5로 나눠 떨어지면, 문제없이 5Kg 봉지만 사용
else:
    for five_bags in range(0, n//5+1):  # 5Kg 봉지를 사용하는 갯수에 따라 순차적으로 돌며 min_bags 갯수 체크
        remain = n - five_bags * 5

        if remain >= 0 and remain % 3 == 0: # 3kg 봉지를 사용해서 N킬로그램을 맞출 수 있는 경우
            three_bags = remain // 3    # 사용하는 3kg 봉지의 갯수를 체크하여
            min_bags = min(min_bags, five_bags + three_bags)    # min_bags에 5kg 봉지 갯수와 3kg 봉지 갯수를 더하여 저장
        
print(min_bags if min_bags != float('inf') else -1) # N킬로그램을 정확하게 맞출 수 없는 경우, min_bags는 그대로 초기값인 무한대 유지 -> -1 출력