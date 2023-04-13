from collections import deque, defaultdict
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
graph_list = [0] + list(map(int, input().split()))

# 직속 부하로 바꿈
graph = defaultdict(list) #[[] for _ in range(n+1)]
for i, g in enumerate(graph_list):
    if i > 1:
        graph[g].append(i)

result = defaultdict(int)
for _ in range(m):
    num, grat = map(int, input().split())
    result[num] += grat


def bfs(start):
    global result
    q = deque([])
    q.append(start)
    while q:
        x = q.popleft()
        w = result[x]
        for pawn in graph[x]:
            result[pawn] += w
            q.append(pawn)

bfs(1)

answer = [0]*(n+1)
for k, i in result.items():
    answer[k] = i

print(*answer[1:])

