# 10:20  ~ 11:20 1시간

# 무조건 끝난다고 가정하고 해보자.

def find_wormhole():
    # 웜홀 같은번호끼리 묶기
    holes = [[] for _ in range(11)]
    for x in range(n):
        for y in range(n):
            if 6 <= board[x][y] <= 10:
                holes[board[x][y]].append((x,y))
    return holes

# 블록 당 이동방향 정의

def move(x, y, d):
    start = (x, y)
    nx, ny = x, y
    score = 0
    while True:
        nx, ny = nx + dx[d], ny + dy[d]
        # print('move by d:', d)
        # print('move to:', (nx, ny))

        # 벽일때
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            score += 1
            d = (d + 2) % 4 # 방향 반대로
            continue
        else:
            if (nx, ny) == start: # 출발점 되돌아오면 끝
                return score
            elif board[nx][ny] == 0:
                continue
            elif 6 <= board[nx][ny] <= 10: # 웜홀
                gates = holes[board[nx][ny]][:] # [(x1, y1), (x2, y2)]
                gates.remove((nx, ny))
                nx, ny = gates[0] # 반대편 웜홀로 위치 이동
                continue
            elif board[nx][ny] == -1: # 블랙홀 빠지면 점수 반환하고 끝
                return score
            else: # board[[nx][ny]] == 1,2,3,4,5
                d = blocks[board[nx][ny]][d] # d를 바꿈
                score += 1
                continue


import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = (-1, 0, 1, 0) # 상 우 하 좌 시계방향
    dy = (0, 1, 0, -1)
    blocks = [None,(2,3,1,0),(1,3,0,2),(3,2,0,1),(2,0,3,1),(2,3,0,1)]
    max_score = 0

    holes = find_wormhole()

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                for d in range(4):
                    score = move(x, y, d)
                    if max_score < score:
                        max_score = score

    print(f'#{test_case} {max_score}')
