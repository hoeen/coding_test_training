import heapq

# bfs - heap으로 최대부터 뽑기

m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]

visited = [[0]*n for _ in range(m)]
before = [[False]*n for _ in range(m)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited[0][0] = 1

q = [(board[0][0], 0, 0)]

while q:
    h, x, y = heapq.heappop(q)
    if before[x][y]:
        continue
    before[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[x][y] > board[nx][ny]:
                visited[nx][ny] += visited[x][y]
                heapq.heappush(q, (-board[nx][ny], nx, ny))
        

print(visited[m-1][n-1])
