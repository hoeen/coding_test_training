import heapq

n, m, x = map(int, input().split())

vertex = [list(map(int, input().split())) for _ in range(m)]
#  시작, 끝, 비용
graph = [[] for _ in range(n+1)]

for st, en, cost in vertex:
    graph[st].append((en, cost))


INF = int(1e9)

def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue 
        for node, cost in graph[now]:
            if dist + cost < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))
    return distance

max_dist = 0
for st in range(1, n+1):
    route = dijkstra(st)[x] + dijkstra(x)[st]
    if max_dist < route:
        max_dist = route
print(max_dist)




