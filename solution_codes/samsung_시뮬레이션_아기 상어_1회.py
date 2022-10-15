# ~ 18:10 현재 40분 소요
# 20분 내 정리하기
def find_shark():
    for x in range(n):
        for y in range(n):
            if board[x][y] == 9:
                return x, y

def bfs(x, y):
    global size
    # 행, 열 순으로 찾는다.
    q = deque([])
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    q.append((x, y, 0))
    catch = []
    
    while q:
        qx, qy, qd = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    # 빈칸
                    if board[nx][ny] == 0 or board[nx][ny] == size:
                        visited[nx][ny] = True
                        q.append((nx, ny, qd+1))
                    elif board[nx][ny] < size:
                        visited[nx][ny] = True
                        catch.append((qd+1, nx, ny))
                        
        # 여기 불안함..
        # if catch:
        #     break
    if catch:
        return sorted(catch)[0][1], sorted(catch)[0][2], sorted(catch)[0][0]
    else:
        return False, False, False # 못잡았으니 리턴




# import sys
from collections import deque

# sys.stdin = open('solution_codes/input.txt', "r")
# sys.stdin = open('input.txt', "r")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 0 빈칸 , 1~6 물고기 크기, 9 상어 위치
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


# 상어 찾기
sx, sy = find_shark()
size = 2
time = 0
bucket = 0
# 상어 이동
while True:
    # 물고기 찾기
    next_x, next_y, dist = bfs(sx, sy)
    # 더이상 먹을 수 있는거 없으면 끝
    if next_x is False:
        break
    time += dist
    # 거리가 가까운 물고기 먹음
    board[sx][sy] = 0
    sx, sy = next_x, next_y # 이동
    board[sx][sy] = 9 # 이동한 자리는 상어
    bucket += 1

    if bucket == size:
        bucket = 0
        size += 1

print(time)
