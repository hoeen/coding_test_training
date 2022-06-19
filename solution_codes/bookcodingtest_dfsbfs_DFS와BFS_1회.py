'''
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
 탐색을 시작할 정점의 번호 V가 주어진다. 
 
 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
 
 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''
from collections import deque

n,m,v = map(int, input().split())

link = []
for _ in range(m):
    a, b = map(int, input().split())
    if a <= b:
        link.append([a,b])
    else:
        link.append([b,a])

# n,m,v = 1000, 1, 1000
# link = [ 
#     [999,1000]
# ]

link = sorted(link)
### dfs
visited = [v]    # 방문

def dfs(node):
    for a, b in link:
        if a == node and b not in visited:
            visited.append(b)
            dfs(b)  
        elif b == node and a not in visited:
            visited.append(a)
            dfs(a)

        # print(a,b)


dfs(v)
# print('dfs')
# print(visited)
for i in range(len(visited)):
    if i == len(visited)-1:
        print(visited[i])
    else:
        print(visited[i], end=' ')


### bfs
q = deque([])

bfs_visit = [v]
q.append(v)


def bfs():
    while q:
        node = q.popleft()
        for a, b in link:
            if a == node and b not in bfs_visit:
                bfs_visit.append(b)
                q.append(b)
            elif b == node and a not in bfs_visit:
                bfs_visit.append(a)
                q.append(a)
bfs()

# print('bfs')
for j in range(len(bfs_visit)):
    if j == len(bfs_visit)-1:
        print(bfs_visit[j])
    else:
        print(bfs_visit[j], end=' ')
    
    
    

    
    

    
