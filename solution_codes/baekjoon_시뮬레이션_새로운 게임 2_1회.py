# 11:30 시작  12:10 40분   2:17 끝냄.. 총 2시간 47분 소요
def init_pos(players):
    global p_board
    for i, (x, y, d) in enumerate(players):
        p_board[x][y].append([i, d])
    return

def move(x, y, group, d):
    # group 을 말 방향에 따라 이동하는데, 빨간색 혹은 흰색에 따라 행동 바뀜
    global p_board
    moved = []
    # 현재 p_board에서 그룹 제거
    p_board[x][y] = p_board[x][y][:-len(group)]
    # p_board에서 이동한 위치에 그룹 추가
    nx, ny = x + dx[d], y + dy[d]
    # 빨간색 - 역순
    if board[nx][ny] == 1:
        group = group[::-1]
    
    p_board[nx][ny] += group
    
    # 변경된 말의 위치, 방향 리턴
    for gi, gd in group:
        moved.append([gi, nx, ny, gd])

    return moved

# 말 번호마다 그룹 확인
# 방향으로 앞칸 탐색해서 방향 바꿈 or 이동 수행
# 그 후 바뀐 것들을 다시 players에 반영하기


def look(x, y, d, i):
    global players
    # x, y 에 있는 말 확인
    toMove = p_board[x][y][:]
    # 대상 위에 말이 있는지 확인
    for j in range(len(toMove)):
        if toMove[j][0] == i: # 말 번호 같으면
            group = toMove[j:] # 자기번호 포함 그룹
            break
    # 이동하려는 방향 앞 칸 확인
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
        # 방향 반대로 바꿈
        if d % 2 == 0:
            d += 1
        else:
            d -= 1
        # 바뀐 방향대로 group 및 players 수정
        players[i] = [x, y, d]
        group[0][1] = d
        # 앞칸 다시 확인
        mx, my = x + dx[d], y + dy[d]
        if mx < 0 or mx > n-1 or my < 0 or my > n-1:
            return # 아무것도 안하고 다음 순서로 넘어감
        else:
            if board[mx][my] == 2:  
                return
            else:
                moved = move(x, y, group, d) # 실제로 말 이동
                for mi, xx, yy, md in moved:
                    players[mi] = [xx, yy, md]


    else:
        if board[nx][ny] == 2:
            if d % 2 == 0:
                d += 1
            else:
                d -= 1
            # 바뀐 방향대로 group 및 players 수정
            players[i] = [x, y, d]
            group[0][1] = d
            # 앞칸 다시 확인
            mx, my = x + dx[d], y + dy[d]
            if mx < 0 or mx > n-1 or my < 0 or my > n-1:
                return # 아무것도 안하고 다음 순서로 넘어감
            else:
                if board[mx][my] == 2:
                    return
                else:
                    moved = move(x, y, group, d) # 실제로 말 이동
                    for mi, xx, yy, md in moved:
                        players[mi] = [xx, yy, md]
        else:
            moved = move(x, y, group, d)
            for mi, xx, yy, md in moved:
                players[mi] = [xx, yy, md]

    # print('look: ', i)
    # for p in p_board:
    #     print(p)

        



n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
p_board = [[[] for _ in range(n)] for _ in range(n)]
# 0 흰색 1 빨간색 2 파란색
players = [list(map(int, input().split())) for _ in range(k)]
# [행, 열, 이동방향]
for p in players:
    p[0] -= 1
    p[1] -= 1
    p[2] -= 1


dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0) # 우좌상하


init_pos(players)


# print('board:')
# for b in board:
#     print(b)

# 턴이 진행되는 동안 말을 이동
# 4개 이상 쌓인 말 찾으면 게임 종료 - 턴 번호 반환
turn = 0
found = False
while turn < 1000:
    turn += 1
    for i, (x, y, d) in enumerate(players):
        look(x, y, d, i)
        
        for fx in range(n):
            for fy in range(n):
                if len(p_board[fx][fy]) >= 4:
                    found = True
                    # print('found!')
                    print(turn)
                    break
            if found: break
        if found:break

    # check
    # print(f'turn: {turn}')
    # print('p_board:')
    # for p in p_board:
    #     print(p)

    

    if found:
        break
        

if not found:
    print(-1)
