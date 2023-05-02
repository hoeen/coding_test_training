# 완성까지 걸리는 최소시간
# 위상 정렬 
# 진입차수 이용
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1) # 해당 노드가 방문되기 위해 먼저 거쳐야하는 노드 수    
coms = [[]] + [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n+1):
    line = coms[i]
    for node in line[1:-1]: # 먼저 지어져야하는 건물 간선에 다음노드 추가
        graph[node].append(i)
        indegree[i] += 1

# 진입차수 0부터 큐에 넣음
q = deque([])
time = [0]*(n+1)
for g in range(1, n+1):
    if not indegree[g]: 
        q.append(g)
while q:
    now = q.popleft()
    time[now] += coms[now][0]
    # 다음 노드의 진입차수를 1 뺀다
    for next_node in graph[now]:
        time[next_node] = max(time[next_node], time[now])
        indegree[next_node] -= 1
        # 새롭게 진입차수 0 되는 노드 삽입
        if indegree[next_node] == 0:
            q.append(next_node)

print(*time[1:])