n = int(input())
costs = list(map(int, input().split()))
m = int(input())

dp = [-1]*(m+1) #0 ~ m
for i in range(n-1, -1, -1): #0~n-1  
    x = costs[i] # 번호 하나 뽑 - 현재 숫자 가격
    for j in range(x, m+1): # 가격 x부터 m까지
        dp[j] = max(i, dp[j], dp[j-x]*10 + i)
        # 현재 숫자, 직전 번호, j-x 한 값에 해당하는 숫자가 있으면 한자리 올림
print(dp[m])
