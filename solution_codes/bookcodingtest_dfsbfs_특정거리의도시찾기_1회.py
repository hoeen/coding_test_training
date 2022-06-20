# dfs - 스택, 재귀
# bfs - 큐, for 
# ~3:30 #33 
from collections import deque
'''
최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램
최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
출발도시 번호 x
'''
import sys
input = sys.stdin.readline
n,m,k,x = map(int, input().split())

connect = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)

# connect = []
# for _ in range(m):
#     connect.append(list(map(int, input().split())))

start = x # 출발도시 
q = deque()
visited = [-1]*(n+1) # 1~n 까지의 방문정보를 거리로 삽입

q.append(start)
visited[start] = 0 # 첫번째 방문처리

while q:
    now = q.popleft() # 들어온 순서로 뻄. FIFO
    # for dpt, arr in connect:
    #     if now == dpt:
    #         if visited[arr] < 0: # 방문 안한 곳이라면
    #             q.append(arr)
    #             visited[arr] = visited[now] + 1 # 연결된 원래곳 거리 + 1
    for arr in connect[now]:
        if visited[arr] < 0:
            q.append(arr)
            visited[arr] = visited[now] + 1
    
if k not in visited:
    print(-1)            

for num in range(len(visited)):
    if visited[num] == k:
        print(num)

  

