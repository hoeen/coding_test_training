from collections import deque

# 노드, 간선 입력받기
v, e = map(int, input().split())
# 모든 노드 진입차수 0으로 초기화
indegree = [0] * (v+1)
# 각 노드 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

# 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때는 차수 0인 노드 큐 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now) # 큐에 들어간 노드 순서대로 출력하면됨
        # 해당 원소와 연결된 노드 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()