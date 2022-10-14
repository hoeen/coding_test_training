# 17:50 # 19:00    # 1시간 40분

def find_shark():
    sharks = []
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                sharks.append((x, y, board[x][y])) #위치, 상어 번호

    return sharks




def move(x, y, shark_num):
    global direc, shark_pos
    # x, y에 있는 상어가 선호하는 방향에 따라 방향 을설정.
    # print(x,y,shark_num)
    arr_list = pref[shark_num][direc[shark_num]]
    empty = False
    mySmellfound = False
    for ar in arr_list:  # [1,4,3,2]
        nx, ny = x + dx[ar], y + dy[ar]
        if 0 <= nx < n and 0 <= ny < n:
            if smells[nx][ny][1] == 0: # 시간이 0이므로 냄새 없음
                empty = True
                direc[shark_num] = ar
                break  # 상어 이동
            elif smells[nx][ny][0] == shark_num: # 냄새가 자기번호
                if not mySmellfound:
                    mySmellfound = True
                    temp_x, temp_y, temp_ar = nx, ny, ar # 임시저장
                    continue
                else:
                    continue
    if empty:
        return nx, ny, shark_num
    else:
        direc[shark_num] = temp_ar
        return temp_x, temp_y, shark_num



# import sys
# sys.stdin = open('input.txt', 'r')

n, m, k = map(int, input().split())   # k 번 이동하면 냄새 없어짐.
board = [list(map(int, input().split())) for _ in range(n)]

direc = [0] + list(map(int, input().split()))  #[ 방향 ]

# m = 1
pref = [[None]] + \
       [[None] + [list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

# print('pref:')
# for p in pref:
#     print(p)

# pref
# [None]
# [None, [4, 4, 3, 1], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1]]
# [None, [4, 3, 1, 2], [2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2]]
dx = (None, -1, 1, 0, 0)  # 위 아래 왼 오
dy = (None, 0, 0, -1, 1)


# 냄새 격자  (번호, 시간)
smells = [[[0,0]]*n for _ in range(n)]


shark_pos = find_shark()   # 상어


# 냄새 뿌림
for sx, sy, sn in shark_pos:
    smells[sx][sy] = [sn, k]

### 1초마다 수행
isShark = True
for i in range(1000):

    # print('=========')
    # print('time:', i+1)

    # 상어 이동
    new_pos = []
    for sx, sy, sn in shark_pos:
        nx, ny, nn = move(sx, sy, sn)
        new_pos.append((nx, ny, nn))

    # print('shark moved:')
    # print(new_pos)

    # 서로 겹치면 작은게 큰거 쫓아냄
    surv_pos = []
    for sx, sy, sn in new_pos:
        lose = False
        temp = new_pos[:]
        temp.remove((sx, sy, sn))
        for tx, ty, tn in temp:
            if (sx, sy) == (tx, ty) and sn > tn: # 겹치는데 자기보다 높은순위
                lose = True
        if not lose:
            surv_pos.append([sx, sy, sn])

    # print('surv sharks:')
    # print(surv_pos)

    # 냄새가 1씩 줄어듬
    for lx in range(n):
        for ly in range(n):
            if smells[lx][ly][1] > 0:
                smells[lx][ly][1] -= 1
    # print('smells after moved:')
    # for s in smells:
    #     print(s)

    # 냄새 뿌림
    for sx, sy, sn in surv_pos:
        smells[sx][sy] = [sn, k]

    # print('new smell:')
    # for s in smells:
    #     print(s)




    if len(surv_pos) == 1:
        print(i+1)
        isShark = False
        break
    else:
        shark_pos = surv_pos[:]



if isShark:
    print(-1)
