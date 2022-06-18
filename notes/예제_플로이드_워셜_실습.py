# 점화식
n = int(input())
k = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    graph[a][b] = c
for x in range(n+1):
    for y in range(n+1):
        if x == y:
            graph[x][y] = 0

# 점화식 -> fab = min(fab, fak+fkb)
for k in range(1,n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k]+graph[k][y])

for g in graph[1:]:
    print(g[1:])
