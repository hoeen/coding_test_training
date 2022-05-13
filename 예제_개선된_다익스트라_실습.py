import heapq

# 6 11
# 1
n, k = map(int, input().split())
start = int(input())
INF = int(1e9)
dist = [INF]*(n+1)


graph = [[] for _ in range(n+1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for b, c in graph[now]: # now로부터 다음, 거리
            cost = distance + c
            if cost < dist[b]:
                dist[b] = cost
                heapq.heappush(q, (cost, b))

dijkstra(start)

for d in dist[1:]:
    print(d)

            
