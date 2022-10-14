# ~12:30

def put_onefish():
    global board
    floor = board[-1]
    min_idx = []
    min_num = min(floor)
    for i in range(n):
        if floor[i] == min_num:
            board[-1][i] = min_num+1

def rotate_90(b):
    return list(zip(*b[::-1]))


def stack():
    global board
    
    # 2개 이상 쌓인거 찾기
    cand_y = []
    for y in range(n):
        for x in range(n):
            if x < n-1 and board[x][y] > 0:
                cand_y.append(y)
                break
    # print('cand_y:', cand_y)
    # to_rotate의 처음과 끝 y값을 찾아서 길이만큼 옮겨 위에 쌓는다
    len_y = cand_y[-1] - cand_y[0] + 1
    to_rotate = []
    len_x = 0
    for x in range(n):
        if board[x][cand_y[0]] > 0:
            to_rotate.append(board[x][cand_y[0]:cand_y[-1]+1])
            len_x += 1
    if len_x > n-1-cand_y[-1]:
        return False
    else:
        for x in range(-1, -(len_x+1), -1):
            # 옮겼으면 원래 자리에서 삭제
            board[x][cand_y[0]:cand_y[-1]+1] = [0]*len_y
    # print('remove bf rotate:')
    # for b in board:
    #     print(b)
    # print('to_rotate:', to_rotate)
    rotated = rotate_90(to_rotate)
    # print('rotated:', rotated)
    for i in range(len(rotated)):
        board[-2-i][cand_y[-1]+1:cand_y[-1]+1+len_x] = rotated[-1-i]
    
    return True

def control_fish():
    new_board = [b[:] for b in board]
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny]:
                            d = abs(board[x][y] - board[nx][ny]) // 5
                            if d:
                                if board[x][y] > board[nx][ny]:
                                    new_board[x][y] -= d
                                    # new_board[nx][ny] += d
                                else:
                                    new_board[x][y] += d
                                    # new_board[nx][ny] -= d
    return new_board

def floor():
    global board
    flist = []
    for y in range(n):
        for x in range(n-1, -1, -1):
            if board[x][y]:
                flist.append(board[x][y])
                board[x][y] = 0
    # if len(flist) > n:
    #     print('len flist exceeds n')
    board[-1] = flist
    return
    
def float_180():
    global board
    len_y = n // 2
    board[-1][:len_y], board[-2][len_y:] = board[-2][len_y:], board[-1][:len_y]
    board[-2][len_y:] = board[-2][len_y:][:][::-1]
    
    len_y2 = len_y // 2
    yi = -1
    for y in range(len_y, n-len_y2):
        board[-1][y], board[-4][yi] = board[-4][yi], board[-1][y]
        board[-2][y], board[-3][yi] = board[-3][yi], board[-2][y] 
        yi -= 1
    
    # print(len_y2, len_y)
    
    # board[-2][len_y:len_y2], board[-3][n-len_y2:] = board[-3][n-len_y2:], board[-2][len_y:len_y2]
    # board[-1][len_y:len_y2], board[-4][n-len_y2:] = board[-4][n-len_y2:], board[-1][len_y:len_y2]
    # board[-4][n-len_y2:] = board[-4][n-len_y2:][:][::-1]
    # board[-3][n-len_y2:] = board[-3][n-len_y2:][:][::-1]



from collections import deque
# import sys

# sys.stdin = open('input.txt', "r")

n, k = map(int, input().split())
init = list(map(int, input().split()))
board = [[0]*n for _ in range(n)] # NxN 보드 안에서 수행

board[-1] = init

# print('init')
# for b in board:
#     print(b)
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
# 어항 정리 과정
count = 0
while True:
# for _ in range(2):
    count += 1
    # 물고기 가장 적은 어항에 물고기 하나 넣음
    put_onefish()

    # 어항 쌓음
    # 처음에 왼쪽 1개 올리기
    board[n-1][0], board[n-2][1] = board[n-2][1], board[n-1][0]
    # 공중부양 후 90도 회전 쌓음
    while True:
        st = stack()
        # print('stack')
        # for b in board:
        #     print(b)
        if not st: break
    
    
    # 어항 물고기 수 조절 - 인접 어항에 대해 물고기 수 차이 구함. 
    board = control_fish()
    # print('1st controlled:')
    # for b in board:
    #     print(b)

    # 어항을 다시 일렬 - 왼쪽 부터, 아래부터 일렬로 정렬
    floor()
    # print('after floor:')
    # for b in board:
    #     print(b)
    # 다시 공중 부양 ㅅㅂ - 왼쪽 반을 180도 회전시켜 위에 쌓는다.  이를 두번 반복한다. 
    float_180()

    # print('after rotate_180:')
    # for b in board:
    #     print(b)
    # 다시 물고기 조절
    board = control_fish()
    # print('2nd controlled:')
    # for b in board:
    #     print(b)

    floor()
    # print('after floor 2nd:')
    # for b in board:
    #     print(b)
    # 물고기 가장 많은 - 적은 <= K 될때 리턴 
    if max(board[-1]) - min(board[-1]) <= k:
        print(count)
        break

