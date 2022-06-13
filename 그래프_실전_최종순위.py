# 위상 정렬 문제
# ? : 여러개의 결과
# imp : 사이클 발생
from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    # n개 이전에 q가 비고 끝나면 사이클 발생함.
    # q에 1개 이상이 들어간다면 여러가지 경로이므로 단일한 순서 아님
    
    
    n_all = 0
    
    while q:
        if len(q) > 1:
            answer.append('?')
            return

        now = q.popleft()
        result.append(now)
        n_all += 1

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if n_all < n:
        answer.append('IMPOSSIBLE')
        return

    answer.append(result)
    return
    
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
t = int(input())
answer = []
for _ in range(t):
    n = int(input())

    # input list 대로 간선 정보 입력 - [낮은] (높은)
    graph = [[] for _ in range(n+1)]
    before = list(map(int, input().split()))
    indegree = [0] * (n+1) # 노드 진입차수
    for i in range(len(before)):
        for g in before[i+1:]:
            graph[g].append(before[i])
            indegree[before[i]] += 1


    # 순위 변경 - 간선 반대로 바꾸기
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]: #순위가 a < b였다면
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1

    topology_sort()

for ans in answer:
    if type(ans) != list:
        print(ans)
    else:
        for i in range(len(ans)-1, -1, -1):
            print(ans[i], end=' ')
        print()

