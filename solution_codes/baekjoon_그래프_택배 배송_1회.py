# ~11:30
import heapq
n, m = map(int, input().split())

# 다익스트라 - 먼저 dist, graph 를 정의
# dist는 무한으로 초기화
INF = int(1e9)
dist = [INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) 
    graph[b].append((a,c))

# 다익스트라 시작 - 먼저 start 노드의 거리를 0으로 하고 q에 넣음
def dijkstra(start):
    q = []
    dist[start] = 0 
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        # cost가 dist[now]보다 작으면, 최단거리후보이므로 q에 넣는 것.
        for next, length in graph[now]:
            # now에서 이어진 next와 길이 length
            if cost + length < dist[next]:
                dist[next] = cost + length
                heapq.heappush(q, (cost + length, next))

dijkstra(1)
print(dist[n])







