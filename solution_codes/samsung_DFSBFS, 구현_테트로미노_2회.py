# 테트로미노 하나를 적절히 놓아 수가 최대가 되도록 하기
# 회전이나 대칭도 가능. -> 길이 4인 dfs
# from collections import deque
import sys
input = sys.stdin.readline

dx = (-1, 0, 1, 0) #시계방향
dy = (0, 1, 0, -1)

max_sum = 0

def dfs(x, y, length, ns):
    global max_sum
    if length > 4:
        if max_sum < ns:
            max_sum = ns
            return
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    ns += board[nx][ny]
                    # 방문 안했을 경우 방문하고 nums에 추가
                    dfs(nx, ny, length+1, ns)
                    visited[nx][ny] = False
                    ns -= board[nx][ny]

def middle(x, y):
    global max_sum
    ds = [[(x-1, y+1), (x-1, y), (x-1, y-1)],
          [(x+1, y+1), (x+1, y), (x+1, y-1)],
          [(x-1, y-1), (x, y-1), (x+1, y-1)],
          [(x-1, y+1), (x, y+1), (x+1, y+1)]
        ]
    for s in ds:
        msum = board[x][y]
        isThree = True
        for nx, ny in s:
            if 0 <= nx < n and 0 <= ny < m:
                msum += board[nx][ny]
            else:
                isThree = False
                break
        if isThree:
            if max_sum < msum:
                max_sum = msum
        # print('middle')
        # print(s)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


visited = [[False]*m for _ in range(n)]
for r in range(n):
    for c in range(m):
        dfs(r, c, 1, 0)
        middle(r, c)

print(max_sum)