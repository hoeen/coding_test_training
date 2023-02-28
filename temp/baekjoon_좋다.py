# 어떤 수가 다른 두 수 두개의 합
# N개의 수 주어지면 좋은수의 개수 몇개인지

# 투포인터
# two-pointer 

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
good = 0

for i in range(n):
    selected = nums[i]
    # 투포인터
    p1 = 0 # 작은곳부터 출발포인터
    p2 = n-1 # 큰곳에서 출발포인터
    while p1 < p2:
        if p1 == i:
            p1 += 1
        if p2 == i:
            p2 -= 1
        if p1 >= p2:
            break
        psum = nums[p1] + nums[p2]
        if psum == selected:
            good += 1
            break
        elif psum < selected:
            p1 += 1
        else:
            p2 -= 1


print(good)