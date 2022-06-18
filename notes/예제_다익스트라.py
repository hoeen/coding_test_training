import sys
# input = sys.stdin.readline()
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF] * (n+1)

# 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
        index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # j = (목적지, 거리)
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단거리 가장 짧은 노드 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: # j = (목적지, 거리)
            cost = distance[now] + j[1] # 거리를 더함
            # 현재 노드를 거쳐가는게 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    # 도달 못하는 경우 무한 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])







