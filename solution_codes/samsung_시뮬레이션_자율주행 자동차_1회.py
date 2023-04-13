# import sys
# import time

# sys.stdin = open('./input.txt', 'r')
# 시계방향 상 우 하 좌
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def move(x, y, d):
    global total
    moved = False
    for _ in range(4):
        d = (d-1)%4 # 좌회전
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                x, y = nx, ny # 이동 
                moved = True
                total += 1
                # print('move!', x, y, d)
                return x, y, d
    if not moved: # 안움직였으면 후진
        d = (d-2)%4 # 반대 
        nx, ny = x + dx[d], y + dy[d]
        if board[nx][ny] == 0:
            x, y = nx, ny # 도로이므로 후진
            d = (d-2)%4 # 방향 원래대로
            return x, y, d
        else:
            # 후진도 못하므로 멈춤
            return None, None, None


n, m = map(int, input().split())
x, y, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 도로 0 인도 1
visited = [[False]*m for _ in range(n)]
visited[x][y] = True
total = 1

#반복
canGo = True
while canGo:
    # print('canGo:', x, y, d)
    x, y, d = move(x, y, d)
    if x == None:
        canGo = False

print(total)