# 최단시간 - bfs
from collections import deque

def solution(l, r, c):
    # 층수, 행 열 수
    board = []
    for li in range(l):
        board.append(
            [list(input()) for _ in range(r)]
            )
        _ = input()

    # 동서 남북 상하
    dx = (-1, 1, 0, 0, 0, 0)
    dy = (0, 0, -1, 1, 0, 0)
    dz = (0, 0, 0, 0, -1, 1)

    q = deque([])

    def find_start_end(l, r, c):
        for z in range(l):
            for x in range(r):
                for y in range(c):
                    if board[z][x][y] == 'S':
                        start = (x, y, z)
                    elif board[z][x][y] == 'E':
                        exit = (x, y, z)
        return start, exit

    visited = [[[-1]*c for _ in range(r)] for _ in range(l)]
    (sx, sy, sz), (ex, ey ,ez) = find_start_end(l, r, c)
    visited[sz][sx][sy] = 0
    q.append((sx, sy, sz))
    while q:
        qx, qy, qz = q.popleft()
        for i in range(6):
            nx, ny, nz = qx + dx[i], qy + dy[i], qz + dz[i]
            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l:
                if visited[nz][nx][ny] < 0 and board[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = visited[qz][qx][qy] + 1
                    q.append((nx, ny, nz))
                    
    if visited[ez][ex][ey] > 0:
        print('Escaped in {} minute(s).'.format(visited[ez][ex][ey]))
    elif visited[ez][ex][ey] == -1:
        print('Trapped!')

while True:
    l, r, c = map(int, input().split())
    # print('l, r, c:', l, r, c)
    if (l, r, c) == (0, 0, 0):
        break
    solution(l, r, c)