# ~ 11:40

dx = (-1, 0, 1, 0) # 상 좌 하 우
dy = (0, -1, 0, 1)

def spread():
    global board
    sp_board = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] != -1:
                sp_count = 0  # 확산된 방의 개수
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c:
                        if board[nx][ny] != -1:
                            sp_board[nx][ny] += (board[x][y]//5)
                            sp_count += 1
                board[x][y] = board[x][y] - (board[x][y]//5*sp_count)
    for x in range(r):
        for y in range(c):
            board[x][y] += sp_board[x][y]

    # print('board:')
    # for b in board:
    #     print(b)
    return

def find_cl():
    for x in range(r):
        if board[x][0] == -1:
            return x, x+1

def wind(): # 바람이 불어서 시계, 반시계로 순환
    x1, x2 = find_cl()
    # x1, y1에서는 위로 반시계
    before = 0
    for y in range(1, c):
        temp = board[x1][y]
        board[x1][y] = before
        before = temp
    for x in range(x1-1, -1, -1):
        temp = board[x][c-1]
        board[x][c-1] = before
        before = temp
    for y in range(c-2, -1, -1):
        temp = board[0][y]
        board[0][y] = before
        before = temp
    for x in range(1, x1):
        temp = board[x][0]
        board[x][0] = before
        before = temp
    # x2, y2에서는 아래로 시계
    before = 0
    for y in range(1, c):
        temp = board[x2][y]
        board[x2][y] = before
        before = temp
    for x in range(x2 + 1, r):
        temp = board[x][c - 1]
        board[x][c - 1] = before
        before = temp
    for y in range(c - 2, -1, -1):
        temp = board[r-1][y]
        board[r-1][y] = before
        before = temp
    for x in range(r - 2, x2, -1):
        temp = board[x][0]
        board[x][0] = before
        before = temp
    # print(x1,y1,x2,y2)
    # print('after wind:')
    # for b in board:
    #     print(b)
    return




r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

# r, c, t = 7, 8, 3
# board = [
# [0, 0, 0, 0, 0, 0, 0, 9],
# [0, 0, 0, 0, 3, 0, 0, 8],
# [-1, 0, 5, 0, 0, 0, 22, 0],
# [-1, 8, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 10, 43, 0],
# [0, 0, 5, 0, 15, 0, 0, 0],
# [0, 0, 40, 0, 0, 0, 20, 0],
# ]
for ts in range(t):
    spread()
    wind()
    # print('elapsed:', ts+1)
    # for b in board:
    #     print(b)
answer = 0
for x in range(r):
    for y in range(c):
        if board[x][y] != -1:
            answer += board[x][y]
print(answer)