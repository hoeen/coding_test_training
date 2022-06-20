# ~3:00 
'''
양방향
소요시간 1
소개팅..  K번 회사에 존재 
1 - K - X 최소시간
X에 도달 못하면 -1 출력 
'''
import heapq

n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


x, k = map(int, input().split())

def dijkstra(start, end):
    dist = [INF]* (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        cost, next = heapq.heappop(q)
        if cost > dist[next]:
            continue
        for node in graph[next]:
            distance = cost + 1
            if distance < dist[node]:
                dist[node] = distance
                heapq.heappush(q, (distance, node))
    
    if dist[end] != INF:
        return dist[end]
    else:
        return False

ans1 = dijkstra(1,k)
ans2 = dijkstra(k, x)
if ans1 and ans2:
    print(ans1 + ans2)
else:
    print(-1)

