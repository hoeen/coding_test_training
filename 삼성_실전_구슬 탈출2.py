from copy import deepcopy
n, m = map(int, input().split())

import sys
input = sys.stdin.readline
# # 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 
# # 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

board = []
for _ in range(n):
    board.append(list(input()))

def find(board): # R,B,O의 위치 반환
    find_list = [[], [], []]
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                find_list[0].append((x,y))
            elif board[x][y] == 'B':
                find_list[1].append((x,y))
            elif board[x][y] == 'O':
                find_list[2].append((x,y))
    return find_list


red, blue, goal = find(board)[0][0], find(board)[1][0], find(board)[2][0]



empty_board = deepcopy(board)

# 구슬이 없는 보드 만들기

empty_board[blue[0]][blue[1]] = '.'
empty_board[red[0]][red[1]] = '.'


# 상하좌우로 끝까지 이동하도록 구성
dx, dy = (-1,0,1,0), (0,-1,0,1)  # 상좌하우


def move(rx, ry, bx, by, dir): # dir 0~3
    rhole, bhole = False, False # 구멍 찾았는지 여부
    rb, bb = deepcopy(empty_board), deepcopy(empty_board)
    rb[rx][ry] = 'R'
    bb[bx][by] = 'B' # 처음 위치를 넣기
    rdist, bdist = 0, 0
    while True: # for red
        rnx, rny = rx+dx[dir], ry+dy[dir]
        if rnx > 0 and rny > 0 and rnx < n-1 and rny < m-1 and rb[rnx][rny] != '#': 
            if rb[rnx][rny] == 'O':
                rhole = True
            else:
                rb[rnx][rny], rb[rx][ry] = rb[rx][ry], rb[rnx][rny]
            rx, ry = rnx, rny
            rdist += 1 
        else:
            break

    while True: # for blue
        bnx, bny = bx+dx[dir], by+dy[dir]
        if bnx > 0 and bny > 0 and bnx < n-1 and bny < m-1 and bb[bnx][bny] != '#': 
            if bb[bnx][bny] == 'O':
                bhole = True
            else:
                bb[bnx][bny], bb[bx][by] = bb[bx][by], bb[bnx][bny]
            bx, by = bnx, bny
            bdist += 1
        else:
            break
    
    # 겹치는지 check
    if (rnx, rny) == (bnx, bny):
        if rdist < bdist:
            # b가 더 많이 움직였으므로 a가 앞에있음. 그러므로 b가 뒤로 한칸 물러나기
            bb[bx][by], bb[bx-dx[dir]][by-dy[dir]] = bb[bx-dx[dir]][by-dy[dir]], bb[bx][by]
        else:
            rb[rx][ry], rb[rx-dx[dir]][ry-dy[dir]] = rb[rx-dx[dir]][ry-dy[dir]], rb[rx][ry]

    return find(rb)[0][0], find(bb)[1][0], rhole, bhole

visited = [(red,blue)]

def bfs():
    q = [[red,blue]]
    rot = 1
    
    while q:
        for _ in range(len(q)):
            rp, bp = q.pop(0)
            
            for dir in range(4):
                zr, zb, rh, bh = move(rp[0],rp[1],bp[0],bp[1],dir)
                if not rh and not bh:
                    if (zr,zb) not in visited:
                        visited.append((zr,zb)) # 방문처리
                        q.append([zr,zb]) # 도착한곳 차례대로 append
                elif rh and not bh:
                    return rot
                else:
                    continue
        if rot == 10:
            return -1
        rot += 1
    return -1

print(bfs())

    
    
    





# def bfs(now_board, count, red_map, blue_map, red_vis, blue_vis):
#     if count == 0:
#         global red_visited, blue_visited, red_board, blue_board, board
#         # visited 초기화 
#         red_vis = [[False]*m for _ in range(n)]
#         blue_vis = [[False]*m for _ in range(n)]
#         # red,blue board 초기화
#         red_map = deepcopy(board)
#         blue_map = deepcopy(board)
    
#     # 공 위치 찾기
#     red, blue, goal = find(now_board)[0][0], find(now_board)[1][0], find(now_board)[2][0]
#     for dir in range(3):
#         # move 각 방향으로 실행. 
#         move(red[0],red[1],dir,'red')
#         move(blue[0],blue[1],dir,'blue')

    
# move(red[0],red[1], 0, 'red') # 상

# red = find(red_board)[0][0]
# move(red[0],red[1], 3, 'red') # 좌

