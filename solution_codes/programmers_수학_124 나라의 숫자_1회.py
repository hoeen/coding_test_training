# ~ 11:30

def solution(n):
    answer = ''
    nums = [0,1,2,4]
    while n > 3:
        div = n // 3
        rem = n % 3
        if rem == 0:
            div -= 1
            rem = 3
        answer = str(nums[rem]) + answer
        n = div
    answer = str(nums[n]) + answer
    return answer

print(solution(25))