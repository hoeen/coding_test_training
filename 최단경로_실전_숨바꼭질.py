import heapq

n, m = map(int, input().split())
# 1번으로부터 가장 먼 헛간 찾기
# 다익스트라

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
dist = [INF] * (n+1)

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        cost = distance + 1
        for next in graph[now]:
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (cost, next))

# 다익스트라 알고리즘 수행하여 dist 갱신
dijkstra(1)

# print('dist')
# print(dist)
# 정답 출력
dmax = max(dist[1:])
nodes = []
for i in range(1, n+1):
    if dist[i] == dmax:
        nodes.append(i)

print(nodes[0], dmax, len(nodes))

    

        