'''
이분탐색
parametric search
주어진 그룹에서 점수 x가 가능한지?
가능하면 더 늘리고, 가능하지 않으면 줄인다.

점수의 최솟값 : x 
x: 10
12 7 19 20 17 14 9 / 10
하지만 이 경우에는 그룹 최댓값이 더 커질 수 있음
x를 하한선으로 하여 

1) 양수이기 때문에 
    만들수 있는 최소한의 그룹을 만든다 -> 그래야 합이 커짐
2) 주어진 x에서 최소한의 그룹을 만들려면? 
    -> 최대한 각 그룹이 x를 채우도록 함 
3) x로 최소한의 그룹을 만들었는데 그룹 수가 넘어가면
    -> 더 큰 x 제한을 두고 그룹 만들기
4) 더 작은 x 경우는?
    -> 그룹수가 k만큼 다다르지 않으면 (제한이 너무 큼)
'''


n, k = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, int(10**5)*20 + 1
value = 0
while start < end:
    mid = (start + end) // 2
    print('mid:', mid)
    # mid 점수를 최대로 할 때 - 그룹 수 체크
    groups = 0
    sum_ = 0
    for i in nums:
        sum_ += i
        if sum_ >= mid:
            sum_ = 0
            groups += 1
        if groups > k:
            break
    if groups >= k:
        value = mid
        # 더 큰 x를 탐색
        start = mid+1
    else: # 생성된 그룹이 너무 적다 -> k를 더 작게
        end = mid-1
        
print(value)


