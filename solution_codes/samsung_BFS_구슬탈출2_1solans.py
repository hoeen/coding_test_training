# ~10:30
# 연결 리스트 구성
# BFS - queue, DFS - stack (재귀)
# 일단, 빨간구슬이 구멍에 들어갈때까지를 구현

### 풀이 
# https://jeongchul.tistory.com/665
## 유형 좀 익힌다음 다시 풀어보기!

from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# visited for [rx][ry][bx][by]  - 두개의 구슬의 x,y동시 체크해야 하므로 4차원으로 선언

dx, dy = (-1,0,1,0), (0,1,0,-1)
q = deque()

def init():   # 시작노드 설정
    rx, ry, bx, by = [0]*4 # 0으로 초기화
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    print(rx, ry, bx, by)
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True # 시작노드 방문처리

# 움직임 구현
def move(x, y, dx, dy):
    count = 0 # 이동한 칸수
    # 다음 이동이 벽이거나 구멍일 때까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


# bfs 탐색
def bfs():
    init()
    while q: # BFS -> queue, while
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(len(dx)):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])

            if board[next_bx][next_by] == 'O':
                continue
            if board[next_rx][next_ry] == 'O':
                print(1)
                return
            # 동시에 같은 칸으로 갈 경우, 많이 움직인것이 뒤로 한칸 가면 된다.
            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]

            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth + 1))
    print(0)

bfs()