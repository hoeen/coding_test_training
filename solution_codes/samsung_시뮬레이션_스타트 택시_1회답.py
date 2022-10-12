# 18:16 ~ 19:00 # 35분
# 23:40 ~ 00:25  45분 총 80분 
# 최단경로로만 이동
# 연료 한칸이동마다 1만큼 소모
# 목적지로 운송 성공하면 소모한 연료 양의 2배 충전
# 연료 바닥나면 끝. 바닥나면서 운송 성공하면 성공으로 침

# 모든 승객을 데려다줄 수 있으면 -> 최종적으로 남는 연료 양 출력하라

dx = (-1, 1, 0, 0) # 상 좌 우 하
dy = (0, 0, -1, 1)
# 가장 가까운 승객. 여러명이면 행 번호가 가장 작은 . 그 중 열 번호가 가장 작은 승객.
def bfs(x, y): # 제일 가까운 승객 찾기
    # 행이 가장 작은 -> 열이 가장 작은
    q = deque([(x, y, 0)])
    visited = [[False]*n for _ in range(n)]
    # bfs로 찾아서 같은 거리에 찾은 사람들을 행, 열 순으로 정렬하여 한명만 뽑는다.
    if psng_map[x][y] and (x, y) not in delivered:  # 처음 위치에 승객 있을경우
        return 0, psng_map[x][y][0] # 소요 거리 및 승객 숫자 반환
    visited[x][y] = True
    same_dist = []
    min_found = None
    while q:
        qx, qy, qd = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] != 1:
                    if psng_map[nx][ny] and (nx, ny) not in delivered:
                        if not same_dist:
                            same_dist.append((nx, ny))
                            min_found = qd
                        elif qd == min_found:
                            same_dist.append((nx, ny))
                    else:
                        q.append((nx, ny, qd+1))
                    visited[nx][ny] = True
    if same_dist:
        sx, sy = sorted(same_dist)[0]
        return min_found+1, psng_map[sx][sy][0]
    
    # print('psg not found!')
    return False, False


def go(psng_id): # 목적지로 데려다 주고 dist 반환
    q = deque([])
    px, py, pgx, pgy = psng[psng_id]
    visited = [[False]*n for _ in range(n)]
    q.append((px, py, 0))

    while q:
        qx, qy, qd = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] != 1:
                    if (nx, ny) == (pgx, pgy):     # 목적지 도달하면
                        return qd+1 # 거리 반환
                    else:
                        q.append((nx, ny, qd+1))
                    visited[nx][ny] = True
    # 못 데려다줄경우
    return False
                        


import sys
from collections import deque
# sys.stdin = open('solution_codes/input.txt', "r")
sys.stdin = open('input.txt', 'r')

n, m, gas = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
psng = [list(map(int, input().split())) for _ in range(m)] # x, y, gx, gy
psng = [[x-1, y-1, gx-1, gy-1] for (x, y, gx, gy) in psng]

# 승객 map
psng_map = [[[] for _ in range(n)] for _ in range(n)]
# 도착지 map
# dest_map = [[-1]*n for _ in range(n)] # 승객 번호가 표시됨
for i, (px, py, pdx, pdy) in enumerate(psng):
    psng_map[px][py] = [i, pdx, pdy]
    # dest_map[pdx][pdy] = i

possible = True
delivered = []  # 승객 시작위치를 넣음

def activate(gas):
    # breakpoint()
    tx, ty = sx, sy # 처음은 시작점
    while True:
        dist, pi = bfs(tx, ty) # 가까운 승객 찾아서 거리와 번호 반환
        if dist is False:
            return -1
        gas -= dist # 연료 소모
        if gas <= 0:
            return -1
        cost = go(pi)# 찾았으면 데려다 줘야지
        tx, ty = psng[pi][2], psng[pi][3]
        if cost is False or cost > gas:
            return -1
        # 데려다 줬으면 운송 승객 리스트에 추가
        delivered.append((psng[pi][0], psng[pi][1]))
        gas -= cost
        if gas == 0: # 기름 없을때
            # 남은 승객이 없으면 성공 - 운송한 승객을 더해준 리스트와 길이 비교
            if len(delivered) == len(psng):
                return gas + cost*2
            else:
                return -1
        elif len(delivered) == len(psng):
            return gas + cost*2
        gas += cost*2

print(activate(gas))

    





