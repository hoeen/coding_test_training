from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, list(input()))))

visited = [[False]*m for _ in range(n)]
dx = (-1,1,0,0)
dy = (0,0,-1,1) # 상하좌우
def bfs(): 
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and maze[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

bfs()
print(visited[n-1][m-1])



