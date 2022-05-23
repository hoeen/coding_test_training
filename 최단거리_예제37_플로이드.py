n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 대각선은 0
for x in range(n+1):
    for y in range(n+1):
        if x == y:
            graph[x][y] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c


# 플로이드 워셜
# fab = min(fab, fak + fkb)
for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

# 출력
for x in range(1, n+1):
    for y in range(1, n+1):
        if graph[x][y] == INF:
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print('')

