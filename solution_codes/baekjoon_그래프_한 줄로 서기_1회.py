# 줄을 어떻게 서야 하는지 완성해야 함
from itertools import combinations
from collections import deque
'''
위상 정렬
목적 : '방향성에 거스르지 않도록 모든 노드를 순서대로 나열하는 것'
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음을 반복한다.
    1) 큐에서 원소를 꺼내 해당 노드 출발간선을 그래프에서 제거한다.
    2) 진입차수가 0이 된 노드를 큐에 넣는다.
'''

n = int(input())

left_tall = [0] + list(map(int, input().split()))
# 0 , 2 1 1 0

# 자신보다 키큰사람을 가리키는 간선 그래프 (X)
# 처음 그래프는 자신이외 모든 사람을 가리켜야 함
graph = [[]] + [list(range(1, n+1)) for _ in range(1, n+1)]
for i in range(1, n+1):
    graph[i].remove(i)
print(graph)
 
# graph에서 left_tall 만큼 뽑고, 그것이 위상정렬 되는지 확인하며 진행
comb_graph = [[]] + \
            [list(combinations(graph[i], left_tall[i])) for i in range(1, n+1)]
print(comb_graph)

def dfs(output_graph, t): # -> graph를 반환해야 함
    if t == n:
        print('graph_to_topology:', output_graph)
        result = topology(output_graph)
        if len(result) < n:
            return
        elif len(result) == n:
            print(result)
            return
        
    else:
        new_output = output_graph[:]
        for comb in comb_graph[t]:
            new_output[t] = list(comb)
            dfs(new_output, t+1)
            
def topology(graph):
    indegree = [0]*(n+1)
    for node in range(1, n+1):
        for next in graph[node]:
            indegree[next] += 1
    result = []
    q = deque()

    # 처음은 차수 0인 노드 큐 삽입
    for i in range(1, n+1):
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
    return result




dfs([[] for _ in range(n+1)], 1)



