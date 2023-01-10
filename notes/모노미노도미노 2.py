# 2:50   2시간 10분 소요 ..
# 점수 먼저 얻고 블록 내려온 뒤, 연한 칸에 블록이 있는 경우 처리
# 블록을 놓은 위치가 순서대로 주어졌을 때,
# 얻은 점수 / 파란 + 초록 타일 개수 출력

# 우선 보드 구성
board = [[0]*10 for _ in range(4)] + [[0]*4 for _ in range(6)]

def put_tile(t, x, y):
    global board
    # 제일 오른쪽, 제일 아래쪽으로 타일 놓기
    if t == 1:
        # 타일이 파란색 오른쪽으로 이동
        nx, ny = x, y
        while ny < 9:
            ny += 1
            if board[nx][ny] > 0:  # 이미 블록 있음
                ny -= 1
                break
        board[nx][ny] = 1
        # 타일이 초록색 아래쪽으로 이동
        nx, ny = x, y
        while nx < 9:
            nx += 1
            if board[nx][ny] > 0:  # 이미 블록 있음
                nx -= 1
                break
        board[nx][ny] = 1
    elif t == 2:
        # 타일이 파란색 오른쪽으로 이동
        nx, ny = x, y
        mx, my = x, y + 1
        while my < 9:
            ny += 1
            my += 1
            if board[nx][ny] > 0 or board[mx][my] > 0:  # 이미 블록 있음
                ny -= 1
                my -= 1
                break
        board[nx][ny] = 2
        board[mx][my] = 2
        # 타일이 초록색  아래 이동
        nx, ny = x, y
        mx, my = x, y + 1
        while nx < 9:
            nx += 1
            mx += 1
            if board[nx][ny] > 0 or board[mx][my] > 0:  # 이미 블록 있음
                nx -= 1
                mx -= 1
                break
        board[nx][ny] = 2
        board[mx][my] = 2
    elif t == 3:
        # 타일이 파란색 오른쪽으로 이동
        nx, ny = x, y
        mx, my = x + 1, y
        while ny < 9:
            ny += 1
            my += 1
            if board[nx][ny] > 0 or board[mx][my] > 0:  # 이미 블록 있음
                ny -= 1
                my -= 1
                break
        board[nx][ny] = 3
        board[mx][my] = 3
        # 초록색
        nx, ny = x, y
        mx, my = x + 1, y
        while mx < 9:
            nx += 1
            mx += 1
            if board[nx][ny] > 0 or board[mx][my] > 0:
                nx -= 1
                mx -= 1
                break
        board[nx][ny] = 3
        board[mx][my] = 3

def inspect_remove():  # 행 열 조사해서 가득 찬거 없애기
    global board
    # 파란 색
    blue = [b[6:] for b in board[:4]]
    green = [g[:] for g in board[6:]]
    score = 0
    for by in range(4):
        # 차례대로 한 줄 씩 없애고 왼쪽 것을 모두 당기기
        full = True
        for bx in range(4):
            if blue[bx][by] == 0: # 다 안참
                full = False
                break
        if full:
            score += 1
            # 현재 줄 앞줄까지를 당김
            for br in range(4):
                board[br][:7+by] = [0] + board[br][:6+by]
    for gi in range(4):
        full = True
        for gg in green[gi]:
            if gg == 0:
                full = False
                break
        if full:
            score += 1
            board[4:7+gi] = [[0]*4] + board[4:6+gi]

    return score








    # 초록색

def see_middle():
    # 파란색 중간블록 체크
    mid_result = [False, False]
    for mb in [4,5]:
        for mx in range(4):
            if board[mx][mb] > 0:
                mid_result[mb-4] = True
    mid_count = mid_result.count(True)
    for c in range(mid_count):
        for r in range(4):
            board[r] = [0, *board[r][:-1]]

    # 초록색 중간블록 체크
    mid_result = [False, False]
    for mg in [4,5]:
        for my in range(4):
            if board[mg][my] > 0:
                mid_result[mg-4] = True
    mid_count = mid_result.count(True)
    for c in range(mid_count):
        board[4:] = [[0]*4] + board[4:-1]


n = int(input()) # 블록 놓은 횟수
coms = [list(map(int, input().split())) for _ in range(n)]
# t=1 : 크기 1x1   2: 1x2 가로  3: 2x1 세로
total_score = 0
for t, x, y in coms:

    put_tile(t, x, y)

    score = inspect_remove()

    see_middle()

    total_score += score

print(total_score)

total_blocks = 0
for r in range(6,10):
    for c in range(4):
        if board[c][r] > 0:
            total_blocks += 1
        if board[r][c] > 0:
            total_blocks += 1

print(total_blocks)


