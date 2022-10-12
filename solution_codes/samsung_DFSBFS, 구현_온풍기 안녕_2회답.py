# 18:15 ~ 19:45 1시간 30분
# 22:20 ~ 22:50
'''
0: 빈 칸
1: 방향이 오른쪽인 온풍기가 있음
2: 방향이 왼쪽인 온풍기가 있음
3: 방향이 위인 온풍기가 있음
4: 방향이 아래인 온풍기가 있음
5: 온도를 조사해야 하는 칸
'''

# 오 왼 위 아래 4
def find_fan():
    fans = []
    points = []
    for x in range(r):
        for y in range(c):
            if 0 < board[x][y] < 5:
                # 온풍기 발견
                fans.append((x, y, board[x][y]))
            elif board[x][y] == 5:
                points.append((x,y))
    return fans, points

dx = (None, 0, 0, -1, 1)
dy = (None, 1, -1, 0, 0)

# 시계방향으로 돌리자.
def rotate(rn): # 회전 횟수
    global temp
    # 큐로 잡기
    row, col = len(temp), len(temp[0])
    
    rboard = deque([t[:] for t in temp])
    for _ in range(rn):
        q = deque([])
        for ci in range(col):
            qr = deque([])
            for ri in range(row-1, -1, -1):
                qr.append(rboard[ri][ci])
            q.append(list(qr))
        rboard = deque(list(q))
        row, col = col, row

    return list(rboard)
    # temp = [r[:] for r in rboard]
    # print('rotate check - temp')
    # for t in temp:
    #     print(t)
    # for 
    # for _ in range(rn):
    #     temp = [list(z) for z in zip(*temp[::-1])]

def rotate_fan(x, y, row, col, rn):
    for _ in range(rn):
        x, y = y, row-1-x
        row, col = col, row
    return x, y

def rotate_walls(rn, row, col):  # 회전 전의 세로길이 r을 넣어줌
    rotated_walls = [w[:] for w in walls]
    for _ in range(rn):
        new_walls = []
        for x, y, b in rotated_walls:
            if b == 0:
                new_walls.append([y, row-1-x, 1])
            else:
                new_walls.append([y+1, row-1-x, 0])
        rotated_walls = [nw[:] for nw in new_walls]
        row, col = col, row

    return rotated_walls



rot_dic = [None, 0, 2, 1, 3] # 인덱스 방향에서 회전시켜야할 횟수

# 온풍기마다 보드를 따로 주어서 temp 에 더한다.
def wind(fx, fy, fd):
    global temp

    # 오른쪽으로 나오는걸로 고정
    # temp 회전시키고, 팬을 회전한 위치에 배치
    # 1 우 -> 0번  2 좌 -> 2번    3 상 -> 1번   4 하 -> 3번
    row, col = len(temp), len(temp[0])
    rot_num = rot_dic[fd]
    temp = rotate(rot_num) # temp 회전
    rotated_walls = rotate_walls(rot_num, row, col)
    fx, fy = rotate_fan(fx, fy, row, col, rot_num)

    # print('rotate time:', rot_num)
    # print('rotated_walls:', rotated_walls)
    # print('rotated_fan:', fx, fy)

    # 바람 나와서 temp 업데이트
    new_row, new_col = len(temp), len(temp[0])
    fan_board = [[0]*new_col for _ in range(new_row)] # 더해줄 fan board
    gy = fy + 1
    count = -1
    tnum = 5
    fan_board[fx][gy] = 5 # 온풍기 바로 앞 숫자 넣기
    while tnum > 1:
        tnum -= 1
        count += 1
        start_x, end_x = fx - count, fx + count
        if gy == new_col-1:
            break
        for gx in range(start_x, end_x+1):
            # 탐색 범위
            # print(gx)
            # if fan_board[gx][gy] > 0:
            if 0 <= gx < new_row and 0 <= gy < new_col:
                if fan_board[gx][gy] > 0:
                    for i, (rx, ry) in enumerate([(gx-1, gy+1), (gx, gy+1), (gx+1, gy+1)]):
                        if 0 <= rx < new_row and 0 <= ry < new_col:
                            # if fan_board[gx][gy] > 0
                            if i == 0: # 오른쪽 위
                                if [gx,gy,0] not in rotated_walls and \
                                    [gx-1,gy,1] not in rotated_walls and \
                                    fan_board[rx][ry] == 0:
                                    fan_board[rx][ry] = tnum
                            elif i == 1:
                                if [gx,gy,1] not in rotated_walls and \
                                    fan_board[rx][ry] == 0:
                                    fan_board[rx][ry] = tnum
                            else:
                                if [gx+1,gy,0] not in rotated_walls and \
                                    [gx+1,gy,1] not in rotated_walls and \
                                    fan_board[rx][ry] == 0:
                                    fan_board[rx][ry] = tnum
        gy += 1
    # fan_board 를 temp에 더해줌 
    for px in range(new_row):
        for py in range(new_col):
            temp[px][py] += fan_board[px][py]
    
    

    # 4 - 회전수만큼 다시 회전시켜서 원래대로 되돌리기
    rerot_num = (4 - rot_num) % 4
    temp = rotate(rerot_num) # temp 회전
    # if (fx, fy, fd) == (5, 1, 4):
        # print('fan_board after fan:', (fx, fy, fd))
        # for t in zip(*fan_board[::-1]):
        #     print(t)
    

def control_temp():
    new_temp = [t[:] for t in temp]
    for x in range(r):
        for y in range(c):
            for i in range(1,5): # 우 좌 상 하 
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    # 벽 유무
                    if i == 1 and [x, y, 1] in walls:
                        continue
                    elif i == 2 and [x, y-1, 1] in walls:
                        continue
                    elif i == 3 and [x, y, 0] in walls:
                        continue
                    elif i == 4 and [x+1, y, 0] in walls:
                        continue
                    diff = abs(temp[x][y] - temp[nx][ny])//4
                    # if (x, y) == (5, 4):
                        # print('x y nx ny diff:', x, y, nx, ny, diff)
                    if temp[x][y] > temp[nx][ny]:
                        new_temp[x][y] -= diff
                    else:
                        new_temp[x][y] += diff
                        
    return new_temp

def edge_dec():
    global temp
    for ex in range(1, r):
        if temp[ex][0] > 0:
            temp[ex][0] -= 1
    for ex in range(0, r-1):
        if temp[ex][c-1] > 0:
            temp[ex][c-1] -= 1
    for ey in range(0, c-1):
        if temp[0][ey] > 0:
            temp[0][ey] -= 1
    for ey in range(1, c):
        if temp[r-1][ey] > 0:
            temp[r-1][ey] -= 1


def inspect():
    for x, y in points:
        if temp[x][y] < k:
            return False
    return True

# temp = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# nt = rotate()
# for t in nt:
#     print(t)

import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
w = int(input())
walls = [list(map(int, input().split())) for _ in range(w)]
for wi in range(len(walls)):
    walls[wi][0] -= 1
    walls[wi][1] -= 1
# x, y, t
# t = 0 -> (x,y), (x-1, y) / t = 1 -> (x, y), (x, y+1)
temp = [[0]*c for _ in range(r)]
fans, points = find_fan()
choco = 0

# import time

# breakpoint()
# pdb.set_trace()
# tcheck = True
# while tcheck:
while True:
# for _ in range(1):
    # breakpoint()
    # 바람 나옴
    # print('='*10)
    # print('choco:', choco)
    
    # print('init temp:')
    # for t in temp:
    #     print(t)
    # t0 = time.time()
    for fx, fy, fd in fans:
        wind(fx, fy, fd)
    # print(time.time() - t0)
    # print('temp after wind:')
    # for t in temp:
    #     print(t)
    # break
    # 온도 조절
    # temp = [ 
    #     [0,0,0],
    #     [0,46,0],
    #     [0,2,0]
    # ]
    # t0 = time.time()
    temp = control_temp()
    # print(time.time() - t0)
    # print('controlled_temp:')
    # for t in temp:
    #     print(t)
    # break
    # 온도 1이상인 가장 바깥쪽 칸 온도 1 감소
    # t0 = time.time()
    edge_dec()
    # print(time.time() - t0)
    # print('edge dec:')
    # for t in temp:
    #     print(t)
    # 초콜릿 먹음
    choco += 1
    # 모든 칸 온도가 k 이상이면 테스트 중단, 아니면 다시 시작
    if inspect():
        print(choco)
        break
    elif choco > 100:
        print(101)
        break
    
    # tcheck = False

