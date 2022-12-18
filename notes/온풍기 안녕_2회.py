# 18:15 ~ 19:45 1시간 30분

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
    for x in range(r):
        for y in range(c):
            if 0 < board[x][y] < 5:
                # 온풍기 발견
                fans.append((x, y, board[x][y]))
    return fans

dx = (None, 0, 0, -1, 1)
dy = (None, 1, -1, 0, 0)

# 시계방향으로 돌리자.
def rotate(rn): # 회전 횟수
    global temp
    for _ in range(rn):
        temp = [list(z) for z in zip(*temp[::-1])]

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
    # 오른쪽으로 나오는걸로 고정
    # temp 회전시키고, 팬을 회전한 위치에 배치
    # 1 우 -> 0번  2 좌 -> 2번    3 상 -> 1번   4 하 -> 3번
    row, col = len(temp), len(temp[0])
    rot_num = rot_dic[fd]
    rotate(rot_num) # temp 회전
    rotated_walls = rotate_walls(rot_num, row, col)
    fx, fy = rotate_fan(fx, fy, row, col, rot_num)

    # 바람 나와서 temp 업데이트
    new_row, new_col = len(temp), len(temp[0])
    fan_board = [[0]*new_col for _ in range(new_row)] # 더해줄 fan board
    gy = fy + 1
    count = -1
    tnum = 6
    while tnum > 1:
        tnum -= 1
        count += 1
        start_x, end_x = fx - count, fx + count
        for gx in range(start_x, end_x+1):
            # 탐색 범위
            for i, (rx, ry) in enumerate([(gx-1, gy+1), (gx, gy+1), (gx+1, gy+1)]):
                if i == 0: # 오른쪽 위
                    if (x,y,0) not in rotated_walls and \






    # while tnum > 1:
    #     gy += 1
    #     count += 1
    #     tnum -= 1 # 온도 감소
    #     wind_cols = count*2 - 1
    #     start_x, end_x = fx - count, fx + count
    #     for gx in range(start_x, end_x+1):
    #         if 0 <= gx < new_row:
    #             if   # 벽 있는지 확인
    #             temp[gx][gy] += tnum # 온도 업데이트















# temp = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# nt = rotate()
# for t in nt:
#     print(t)




r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
w = int(input())
walls = [list(map(int, input().split())) for _ in range(w)]
# x, y, t
# t = 0 -> (x,y), (x-1, y) / t = 1 -> (x, y), (x, y+1)
temp = [[0]*c for _ in range(r)]
fans = find_fan()
choco = 0

while True:
    # 바람 나옴
    # 먼저 온풍기마다 행렬 회전


    # 온도 업데이트 되면 다시 (4 - 회전수) 만큼 회전해서 원래대로

    # 온도 조절
    temp()
    # 온도 1이상인 가장 바깥쪽 칸 온도 1 감소
    edge_dec()
    # 초콜릿 먹음
    choco += 1
    # 모든 칸 온도가 k 이상이면 테스트 중단, 아니면 다시 시작
    if inspect():
        print(choco)
        break
    elif choco > 100:
        print(101)
        break


