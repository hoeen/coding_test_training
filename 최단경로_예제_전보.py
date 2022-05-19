# ~9:20
''' 
c에서 보낸 메시지 받는 도시 개수, 도시들이 메시지 받는데까지 걸리는 시간 
다익스트라 / 플로이드 워셜? 
c에서 각 도시까지 최단시간 구하고, inf 아닌 도시들의 시간을 더한다.
'''
import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    dist = [INF]* (n+1)
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cost, next = heapq.heappop(q)
        if cost > dist[next]:
            continue
        for node, distance in graph[next]:
            time = cost + distance
            if time < dist[node]:
                dist[node] = time
                heapq.heappush(q, (time, node))
    return dist
dist = dijkstra(c)
count = 0
total_time = 0
for i in range(1,len(dist)):
    cons = dist[i]
    if 0 < cons < INF:
        count += 1
        total_time = max(total_time, cons)

# print(dist)
print(count, total_time)
    




    
