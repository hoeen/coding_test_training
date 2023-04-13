n = int(input())
k = int(input())

# i개 색중 j개 색을 선택하는 경우의수 dp
# i : 1~n
# j : 1~k
dp = [[0]*k for _ in range(n)]
for i in range(0, n):
    dp[i][0] = i+1

for i in range(3, n):
    for j in range(1, k):
        if j <= i/2:
            dp[i][j] = dp[i-1][j] + dp[i-2][j-1]

print(dp[n-1][k-1] % 1_000_000_003)