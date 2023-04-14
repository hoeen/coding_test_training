from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def move(x, y, d, r, c, board):
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            return x, y
        if board[nx][ny] == 'D':
            return x, y
        x, y = nx, ny
        
def bfs(x, y, visited, r, c, board):
    q = deque([])
    visited[x][y] = 0
    q.append((x, y))
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx, ny = move(qx, qy, i, r, c, board)
            if visited[nx][ny] < 0:
                visited[nx][ny] = visited[qx][qy] + 1
                if board[nx][ny] == 'G':
                    return visited[nx][ny]
                q.append((nx, ny))
    return -1

def solution(board):
    # 최단경로 : bfs (미로 등, 끝까지 탐색할 필요 없음. DFS는 끝까지 왔다가 돌아가기 때문에 비효율적일 수 있다)
    r = len(board)
    c = len(board[0])
    visited = [[-1]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] == 'R':
                return bfs(x, y, visited, r, c, board)