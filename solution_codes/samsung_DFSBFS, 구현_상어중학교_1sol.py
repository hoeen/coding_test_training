# 4:26 ~ 6:26
'''
1. 가장 큰 그룹 찾기.
  만약 여러개그룹이면 무지개가 가장 많은 그룹.
  그것도 여러개라면 기준블록의 행이 가장 큰것(가장 아래)
  그것도 여러개면 열이 가장 큰것 (가장 오른쪽)
2. 찾은 그룹의 모든 블록을 제거.
  이때 제거한 블록수를 B라 했을때 B^2 점 획득.
3. 격자 중력 작용
  중력이 작용하면 검정을 제외한 모든 블록이 아래로 이동해서 쌓임.
4. 격자가 90도 반시계 회전
5. 다시 격자에 중력 작용
'''

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# n,m = 5,3
# board = [ 
#     [2, 2, -1, 3, 1],
#     [3, 3, 2, 0, -1],
#     [0, 0, 0, 1, 2],
#     [-1, 3, 1, 3, 2],
#     [0, 3, 2, 2, 1]
# ]

dx = (-1,1,0,0) # 상하좌우
dy = (0,0,-1,1)

# 1. 크기가 가장 큰 블록 그룹 찾기
def bfs():
    block_list = {}
    visited = [[False]*n for _ in range(n)]
    # 먼저 안방문한 일반블록 찾기
    for ix in range(n):
        for iy in range(n):
            # 일반 블록 찾기
            if not visited[ix][iy] and \
                board[ix][iy] > 0:
                x, y = ix, iy
                # print('start:', x, y)
                # 찾고나면, bfs로 그룹 만들고 크기랑 기준블록 넣기
                q = []
                q.append((x,y))
                color = board[x][y]
                visited[x][y] = True
                group = [(x,y,color)] # 기준블록 빼기위해서 찾은것 넣는그룹. 위치,색상
                while q:
                    # print(i)
                    qx, qy = q.pop(0)
                    for i in range(4):
                        nx, ny = qx+dx[i], qy+dy[i]
                        # 검 안되고, 범위 내, 숫자 같아야함, 방문 안해야함
                        if (0 <= nx < n and 0 <= ny < n):
                            if board[nx][ny] != -1 and not visited[nx][ny] and \
                                    (board[nx][ny] == color or board[nx][ny] == 0):
                                q.append((nx,ny))
                                # if board[nx][ny] == 0:  # 무지개는 방문 미처리 - 무한루프됨..
                                #     visited[nx][ny] = False
                                # else:
                                visited[nx][ny] = True
                                # print('block added,', nx, ny)
                                group.append((nx,ny,board[nx][ny]))
                # group에 있는 무지개 블록의 경우 다시 미방문처리로 되돌리기
                rainbow = [(r[0],r[1]) for r in group if r[2] == 0]
                for rx, ry in rainbow:
                    visited[rx][ry] = False
                # 찾은 그룹의 size >= 2 이면 기준블록과 사이즈를 추가
                group = list(set(group))
                # print('group:', group)
                if len(group) >= 2:
                    stx, sty = [(s[0],s[1]) for s in sorted(group) if s[2] > 0][0]
                    # rainbow 크기 추가
                    rain = len([r for r in group if r[2] == 0])
                    # print(group)
                    # print('res:', stx, sty, len(group))
                    block_list[(len(group),rain,stx,sty)] = group        
    
    return block_list

def rem_big(block_list):
    global score
    # 키를 수, 행, 열 순으로 정렬하여 처음것을 뽑기
    key = sorted(block_list.keys(), reverse=True)[0]
    # print('key:', key)
    # 찾은 그룹을 모두 -2로 만들기
    for bx, by, count in block_list[key]:
        board[bx][by] = -2
    score += key[0]**2


# 중력 작용 # 검은블록 그대로. 나머지는 아래로 쌓임
def gravity():
    for y in range(n):
        for x in range(n-1,-1,-1):
            if board[x][y] > -1:
                nx, ny = x, y
                color = board[x][y]
                board[x][y] = -2 # 비운다
                while nx < n-1:
                    nx += 1 # 아래로 한칸 이동
                    if board[nx][ny] >= -1:
                        nx -= 1 # 부딪히면 위로 다시 이동
                        break
                board[nx][ny] = color
                    

# 반시계 회전 - (x,y) - ((n-1)-y, x)
def rotate():
    global board
    new_board = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            xp, yp = (n-1)-y, x
            new_board[xp][yp] = board[x][y]

    # 새로운 보드로 바꾸기
    board = [b[:] for b in new_board]

                




score = 0

while True:
    block_list = bfs()
    if not block_list:
        break

    # print('block:')
    # for b in block_list.keys():
    #     print(b, block_list[b])

    rem_big(block_list)
    # print('removed_block:')
    # for b in board:
    #     print(b)
    # print(score)

    gravity()
    # print('gravity:')
    # for b in board:
    #     print(b)
    rotate()
    # print('rotate:')
    # for b in board:
    #     print(b)

    gravity()
    # print('2gravity')
    # for b in board:
    #     print(b)
    # print('='*30)

print(score)       



