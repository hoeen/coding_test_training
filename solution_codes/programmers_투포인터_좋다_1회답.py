## 시도 2 : 투포인터
# 한 숫자가 다른 두 수로 표현되는지를 한 숫자를 제외한 리스트에서 투포인터로 접근.
# -5 -5 -4 -3 1 2 2 3
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
goods = 0
for i in range(n):
    ex_list = nums[:i] + nums[i+1:]
    left, right = 0, n-2
    while left < right:
        sum_ = ex_list[left] + ex_list[right]
        if sum_ == nums[i]:
            goods += 1
            break
        elif sum_ > nums[i]:
            right -= 1
        else:
            left += 1
print(goods)


## 시도 1 : Counter 과 set을 이용함 -> 다른 두 수의 합을 고려 못함..
# n = int(input())
# nums = list(map(int, input().split()))
# from collections import Counter
# good = 0

# sums = set()
# for i in range(1, n):
#     for j in range(i):
#         sums.add(nums[i]+nums[j])

# counter = Counter(nums)
# print('sums:', sums)
# print('set_counter:', set(counter.keys()))
# good_set = sums & set(nums)
# print('good_set:', good_set)
# for g in good_set:
#     good += counter[g]
# print(good)