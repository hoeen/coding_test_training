import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for a, b, cost in paths:
        graph[a].append((b, cost)) # 다음노드, 거리
        graph[b].append((a, cost)) # 양방향
    
    # 출입구 하나 정하고, 산봉우리 중 하나 방문, 다시 출입구로 돌아옴
    # 이 코스에서 최대거리가 최소일 때 산봉우리와 최대거리를 리턴
    # 최소 여러개면 산봉우리 번호 낮은거를 리턴
    
    # 다익스트라 변형 - 최소 거리를 합산하는게 아니라, 그냥 최대 거리만 남겨둔다
    # 1 - 5 - 1 일때, 1 - 5 에서 최대 거리만 남겨두고, 다시 5 - 1 에서 최대 거리만 남겨둔다
    INF = int(1e9)
    def dijkstra(gates):
        distance = [INF]*(n+1) 
        
        q = []
        
        for g in gates:
            heapq.heappush(q, (0, g)) 
            distance[g] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist or now in summits:
                continue
            for next_node, next_dist in graph[now]:
                cost = max(next_dist, dist) # 변형
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
        return distance
    
    
    sum_list = []
    g_dist = dijkstra(gates)
    for s in summits:
        heapq.heappush(sum_list, (g_dist[s], s))
    intensity, sum_num = heapq.heappop(sum_list)
        
    return [sum_num, intensity]