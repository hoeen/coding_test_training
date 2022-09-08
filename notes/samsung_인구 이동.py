# 10:50
# import sys
from collections import deque
# input = sys.stdin.readline
n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# n, l, r = 2, 20, 50
# board = [ 
#     [100, 50],
#     [1, 2]
# ]


# 인접한 칸 사이에 인구 차 체크 -  국경선 열기
# 연합이 이미 이루어졌는지 여부 체크


dx = (-1, 1, 0, 0) # 상하좌우
dy = (0, 0, -1, 1)
# BFS로 차이 체크하고 연결 - 같은 연합끼리 평균냄
def bfs(x, y):
    # print('bfs result:', x, y)
    global board, unioned
    visited = [[False]*n for _ in range(n)]
    q = deque([(x, y)])
    while q:
        qx, qy = q.popleft()
        # visited[qx][qy] = True
        # unioned[qx][qy] = True
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(board[qx][qy] - board[nx][ny]) <= r \
                    and not visited[nx][ny] and not unioned[nx][ny]:
                    visited[nx][ny] = True
                    unioned[nx][ny] = True
                    q.append((nx, ny))
    # 연합 형성했으면 visited == True인 경우에 평균내기
    ppl = list()
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                ppl.append(board[x][y])
    un_ppl = sum(ppl) // len(ppl)
    # 평균값을 연합에 적용하기
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                board[x][y] = un_ppl

    # check
    
    # print('visited:')
    # for v in visited:
    #     print(v)
    # print('dfs changed:')
    # for b in board:
    #     print(b)
    # print('union changed:')
    # for u in unioned:
    #     print(u)

    return

# 모든 칸에서 국경선 못 열때까지 반복

elapsed = 0
while True:
    open_gate = False
    unioned = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not unioned[x][y]: # 연합 안된경우
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if l <= abs(board[x][y] - board[nx][ny]) <= r and \
                            not unioned[nx][ny]:
                            open_gate = True
                            # print('to bfs found:', nx, ny)
                            bfs(x, y)
                            break
    # check
    # print('day closed, unioned:')
    # for u in unioned:
    #     print(u)
    if open_gate:
        elapsed += 1
    else:
        break

print(elapsed)
        