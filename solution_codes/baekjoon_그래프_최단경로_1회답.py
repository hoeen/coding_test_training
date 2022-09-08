import heapq, math

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


INF = math.inf
distance = [INF]*(v+1)

# 다익스트라
def dijkstra(start):
    q = []
    # 시작 노드 최단 경로는 0으로 설정하고 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 제일 짧은 거리부터 불러옴
        if dist > distance[now]: # 이미 거리가 짧은 경우 갱신 필요 없음
            continue
        for next, length in graph[now]:
            cost = dist + length
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))



dijkstra(start)
for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)