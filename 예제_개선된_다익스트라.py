''' 
직관적 다익스트라는 시간복잡도가 O(V^2)이다. 
개선된 다익스트라는 시간복잡도가 O(ElogV)이다. E는 간선, V는 노드
최단거리가 가장 짧은 노드를 찾기 위해서 매번 최단 거리 테이블을 선형적으로 탐색하는 기존방법에 비해,
heapq(우선순위 큐)를 이용하여 더 빨리 탐색이 가능하다. - 우선순위 큐는 우선순위가 제일 높은 데이터를 먼저 꺼냄.
BFS 의 원리와 비슷하게 동작한다.
'''

import heapq

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드 최단 경로는 0으로 설정. 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        # 가장 최단 거리 짧은 노드 정보 꺼내기. 여기에서 get_smallest_node()를 따로 작성할필요가 없음.
        dist, now = heapq.heappop(q)
        # 현재 노드가 처리된 적이 있는 노드면 무시
        if distance[now] < dist:
            continue
        # 현재와 인접한 다른 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드 거치는게 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])



