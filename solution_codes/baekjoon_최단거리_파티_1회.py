import heapq

n, m, x = map(int, input().split())
input_list = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]

for start, end, dist in input_list:
    graph[start].append((dist, end)) # 거리, 다음노드 

def dijkstra(start):
    q = []
    INF = int(1e9)
    dist = [INF] * (n+1)
    # start 부터 거리 0으로 q에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        now_dist, now_node = heapq.heappop(q)
        if dist[now_node] < now_dist:
            continue
        for next_dist, next_node in graph[now_node]:
            cost = now_dist + next_dist # 힙에서 나온 거리 + 그래프 간선 거리
            if cost < dist[next_node]: # 다음 노드까지의 최단거리보다 cost가 작으면 갱신
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node)) # 갱신한 다음노드와 다음노드까지의 거리를 힙에 삽입
        
    return dist

total_dist = [0]*(n+1)
for i in range(1, n+1): #1~n
    total_dist[i] += dijkstra(i)[x]
    total_dist[i] += dijkstra(x)[i]


print(max(total_dist[1:]))
