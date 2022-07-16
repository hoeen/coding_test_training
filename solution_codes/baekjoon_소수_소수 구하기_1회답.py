# 에라토스테네스의 체
import math

m, n = map(int, input().split())
# m,n = 3, 16
isnum = [True]*(n+1)
isnum[1] = False
isnum[0] = False
for i in range(2, int(math.sqrt(n))+1): 
    #소수 2부터 가장 큰수의 제곱근까지 배수를 지워나감
    if isnum[i]:
        j = 2 # 자기자신 이외니까 2부터 곱함
        while i*j <= n:
            if isnum[i * j]:
                isnum[i * j] = False
            j += 1
for i in range(m, n+1):
    if isnum[i]:
        print(i)