def solution(n, k, nums):
    # 합이 k에 가장 가까운 조합의 수 구하기
    nums.sort()
    left, right = 0, n-1
    min_diff = float('inf')
    count = 0
    while left < right:
        sum_ = nums[left] + nums[right]
        diff = abs(k - sum_)
        if min_diff > diff:
            count = 1 # 새로운 최솟값 나옴
            min_diff = diff
        elif min_diff == diff:
            count += 1
        
        if sum_ == k:
            left += 1
            right -= 1
        elif sum_ < k:
            left += 1
        else:
            right -= 1

    return count

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solution(n, k, nums))