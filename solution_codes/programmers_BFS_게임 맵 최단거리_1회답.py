from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque([])
    
    dist = [[-1]*m for _ in range(n)]
    q.append((0,0))  # x, y, depth
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    if dist[nx][ny] == -1 or dist[x][y] + 1 < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx,ny))
                    
                    
    return dist[n-1][m-1]