import heapq
INF = int(1e9)

def solution(n, edge):
    # 최단경로 시 간선이 가장 많은 노드의 개수
    # 1번으로부터 최단경로 - 다익스트라
    
    # graph 생성
    graph = [[] for _ in range(n+1)]  # 작은 -> 큰 으로 정렬됨.
    for st, en in edge:   
        graph[st].append(en)
        graph[en].append(st)
    
    # visited = [False]*(n+1)
    distance = [INF]*(n+1)
    
    # 1번의 distance = 0 으로 초기화
    distance[1] = 0
    
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        # print(q)
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for next_node in graph[now]:
                cost = dist + 1
                if distance[next_node] > cost:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
              
    answer = 0
    max_dist = max(distance[1:])
    for i in range(1, n+1):
        if distance[i] == max_dist:
            answer += 1
    # print(distance[1:])
    # print('end')
    return answer