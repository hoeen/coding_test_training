n,m,k = map(int, input().split())

# n번도시, m개이하의 도시 지나야, k는 노선 개수

graph = [list(map(int, input().split())) for _ in range(k)]
# a, b, 기내식 c

# dp
# i+1번도시 : max(i+1로 오는 경로가 있는 x의 값들)
dp = [[0]*(n+1) for _ in range(n+1)] # 0~n x 0~n
dp_sum = [[0]*(n+1) for _ in range(m+1)] # 0~m X 0~n 

for a, b, c in graph:
    if a < b:  #[도착][출발]
        dp[b][a] = max(dp[b][a], c)
        if a == 1:
            dp_sum[1][b] = max(dp_sum[1][b], c)

for x in range(1, n+1):
    for i in range(1, x):
        # print('x,i:', x,i)
        cost = dp[x][i] 
        if cost:
            for k in range(1, m-1):
                if dp_sum[k][i]:
                    dp_sum[k+1][x] = max(dp_sum[k+1][x], dp_sum[k][i] + cost)
  
print(max(d[n] for d in dp_sum))