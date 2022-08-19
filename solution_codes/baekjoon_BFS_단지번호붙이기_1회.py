from collections import deque
n = int(input())
board = [list(map(int, input())) for _ in range(n)]

count = []
visited = [[False]*n for _ in range(n)]
dx = (-1, 1, 0, 0) # 상하좌우
dy = (0, 0, -1, 1)

def bfs(x, y):
    count = []
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        qx, qy = q.popleft()
        count.append((qx, qy))
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    # print('nx, ny to put:', nx, ny)
                    visited[nx][ny] = True
                    q.append((nx,ny))
    # print('bfs count:', len(set(count)))
    return len(set(count))

for x in range(n):
    for y in range(n):
        if board[x][y] == 1 and not visited[x][y]: # 방문 안한 1이면
            count.append(bfs(x, y))
    
print(len(count))
count.sort()
for c in count:
    print(c)

    

    


