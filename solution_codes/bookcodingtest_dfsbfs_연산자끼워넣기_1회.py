from itertools import permutations

n = int(input())

nums = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())
cal_list = ''
for i in range(pl):
    cal_list += '+'
for i in range(mi):
    cal_list += '-'
for i in range(mu):
    cal_list += '*'
for i in range(di):
    cal_list += '/'

perm = list(set(permutations(cal_list)))

# 연산자에서 하나씩 빼고 셈을 한다. 
minimal = 0
maximal = 0

checked = False
for p in perm:
    for i in range(len(nums)):
        if i == 0:
            ans = nums[i]
        else:
            j = i-1
            if p[j] == '+':
                ans += nums[i]
            elif p[j] == '-':
                ans -= nums[i]
            elif p[j] == '*':
                ans *= nums[i]
            elif p[j] == '/':
                if ans >= 0:
                    ans //= nums[i]
                else:
                    ans = -(abs(ans) // nums[i])
    if not checked:
        minimal = ans
        maximal = ans
        checked = True
    else:
        minimal = min(minimal, ans)
        maximal = max(maximal, ans)

print(maximal)
print(minimal)

            
    
    