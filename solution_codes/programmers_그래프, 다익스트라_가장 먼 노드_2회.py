from heapq import heappush, heappop

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)] # 각 노드별 이어진 다음 노드와 거리 넣기
    
    for st, en in edge:
        graph[st].append(en)
        graph[en].append(st)
    
    distance = [int(1e9)]*(n+1)
    q = []
    
    def dijkstra(start):
        distance[start] = 0
        heappush(q, (0, start))
        while q:
            dist, now = heappop(q)
            if distance[now] < dist: # 큐에서 꺼낸 거리보다 이미 더 작음
                continue
            for node in graph[now]:
                cost = dist + 1
                if cost < distance[node]:
                    # 큐에서 꺼낸 dist + 다음노드까지의 거리 = cost 가
                    # distance의 다음노드 거리보다 짧으면 갱신하고, 이 거리가 최소이기 때문에 큐에 넣음
                    distance[node] = cost
                    heappush(q, (cost, node))
                    
    dijkstra(1)

    
    return distance[1:].count(max(distance[1:]))