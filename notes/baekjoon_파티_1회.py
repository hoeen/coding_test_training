# ~4:40
# 그래프 문제?
import heapq

n, m, x = map(int, input().split())
#start, end, cost
inp_list = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for start, end, cost in inp_list:
    graph[start].append((end, cost))

# 다익스트라 - i번째 마을에서 X번 마을로 갔다가, 다시 i로 돌아오는 최단거리
INF = int(1e9)

# for start, end, cost in graph:
def dijkstra(start):
    # heap 에 스타트 삽입
    q = []
    dist = [INF]*(n+1)
    dist[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist_now, node_now = heapq.heappop(q)
        if dist[node_now] < dist_now:
            continue
        for node_next, dist_next in graph[node_now]:
            cost = dist_next + dist[node_now]
            if dist[node_next] > cost:
                dist[node_next] = cost
                heapq.heappush(q, (cost, node_next))
        
    return dist

total_dist = [0]*(n+1)
for i in range(1, n+1):
    total_dist[i] += dijkstra(i)
    # print('godist:', godist)
    total_dist[i] += dijkstra(x)[i]
    backdist = dijkstra(x, backdist)
    # print('backdist:', backdist)
    total_dist[i] += backdist[i]

print(total_dist)
print(max(total_dist))