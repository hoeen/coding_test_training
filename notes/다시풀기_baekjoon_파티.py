# 플로이드 워셜

n, m, x = map(int, input().split())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]


for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = cost

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j] = 0

for k in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][k]+graph[k][end])
   

max_dist = 0
for i in range(1, n+1):
    go_back = graph[i][x] + graph[x][i]
    if go_back > max_dist:
        max_dist = go_back

print(max_dist)

            