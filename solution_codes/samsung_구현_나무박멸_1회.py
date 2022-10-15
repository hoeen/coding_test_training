
# 14:40
def grow():
    new_board = [b[:] for b in board]
    for x in range(n):
        for y in range(n):
            if board[x][y] is not None:
                if board[x][y] > 0:
                    to_grow = 0
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] is not None:
                                if board[nx][ny] > 0:
                                    to_grow += 1
                    new_board[x][y] += to_grow  # 나무의 성장
    return new_board

def breed():
    new_board = [b[:] for b in board]
    for x in range(n):
        for y in range(n):
            if board[x][y] is not None:
                if board[x][y] > 0:
                    to_breed = []
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] is not None:
                                if board[nx][ny] == 0:
                                    to_breed.append((nx, ny))
                    if not to_breed:
                        continue
                    else:
                        plus = board[x][y] // len(to_breed)
                        for (bx, by) in to_breed:
                            new_board[bx][by] += plus
    return new_board

def sim_pesti(x, y): # x,y 에 제초제 뿌릴때 전파 수 반환
    dtrees = 0 # 제거된 나무 수
    if board[x][y] >= 0:
        dtrees += board[x][y]
    # 대각선 방향으로 k만큼 전파. -1, 0까지는 전파되고 그 이후 로x
    for d in range(4):
        for i in range(1, k+1): # 1~k
            nx, ny = x + ix[d]*i, y + iy[d]*i
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] is not None:
                    if board[nx][ny] > 0:
                        dtrees += board[nx][ny]
                    else: break
                else: break

    return dtrees

def pesti(x, y):
    global board
    dtrees = 0
    if board[x][y] >= 0:
        dtrees += board[x][y]
    board[x][y] = -(c+1)
    for d in range(4):
        for i in range(1, k+1):
            nx, ny = x + ix[d]*i, y + iy[d]*i
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] is None:
                    break
                elif board[nx][ny] <= 0: # 0 혹은 제초제 빈칸
                    board[nx][ny] = -(c+1)
                    break
                else:
                    dtrees += board[nx][ny]
                    board[nx][ny] = -(c+1)
    return dtrees



#
# import sys
# sys.stdin = open('input.txt', "r")

n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 빈칸 0  벽 -1 -> None으로 하기 . 제초제 를음수로 잡기
for x in range(n):
    for y in range(n):
        if board[x][y] == -1:
            board[x][y] = None


dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
ix = (-1, -1, 1, 1)
iy = (-1, 1, 1, -1)

total_remove = 0
for y in range(m):
    # print('year:', y + 1)

    # 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다.
    # 4개 칸 중 빈칸에 번식 (제초제 없는) 시작
    # 번식 가능한 칸 개수 를세서, 이로 나누어진 그루 수만큼 번식 (몫)
    board = grow()

    # print('grow')
    # for b in board:
    #     print(b)


    board = breed()

    # print('breed')
    # for b in board:
    #     print(b)

    # 제초제 뿌림
    # 가장 많이 박멸되는 칸에 제초제
    # 4개의 대각선 방향으로 K만큼 전파 . 벽이나 나무가 없는 칸까지는 전파됨.
    max_eff = 0
    px, py = None, None
    for x in range(n):
        for y in range(n):
            if board[x][y] is not None:
                if board[x][y] > 0:
                    eff = sim_pesti(x, y)
                    if eff > max_eff:
                        px, py = x, y
                        max_eff = eff

    # print(max_eff)
    # print(px, py)
    if px == None:
        continue
    else:
        rem = pesti(px, py)
        total_remove += rem

        # print('removed:', rem)
        # for b in board:
        #     print(b)

        # 제초제 + 1
        # c년만큼 남아있다가 c+1년에 사라짐
        for x in range(n):
            for y in range(n):
                if board[x][y] is not None:
                    if board[x][y] < 0:
                        board[x][y] += 1

        # print('pesti dec')
        # for b in board:
        #     print(b)

# print('total removed:', total_remove)

print(total_remove)