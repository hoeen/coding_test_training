# 1시간 25분 소요
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
di_list = list(map(int, list(input()))) 

# check m  0 부터 숫자 부여
jx, jy = 0, 0
mad_list = []
for x in range(r):
    for y in range(c):
        if board[x][y] == 'R':
            mad_list.append((x, y))
        elif board[x][y] == 'I':
            jx, jy = x, y


dx = (None, 1, 1, 1, 0, 0, 0, -1, -1, -1)
dy = (None, -1, 0, 1, -1, 0, 1, -1, 0, 1)

def which_way(rx, ry):
    min_d = int(1e4)
    for d in range(1, 10): # 한방향이 딱 정해진다고 가정하자
        nx, ny = rx + dx[d], ry + dy[d]
        if 0 <= nx < r and 0 <= ny < c:
            dist = abs(jx - nx) + abs(jy - ny)
            if min_d > dist:
                way = d
                min_d = dist
    return way

j_moved = 0
lose = False

for i, di in enumerate(di_list):
    jx += dx[di]
    jy += dy[di]

    j_moved += 1

    # 미친 아두이노 이동
    moved_list = []
    for mx, my in mad_list:
        way = which_way(mx, my)
        moved_list.append((mx + dx[way], my + dy[way]))
    if (jx, jy) in moved_list:
        print('kraj ' + str(j_moved))
        lose = True
        break

    # 중복되는것 같이 삭제
    if len(set(moved_list)) != len(moved_list):
        moved_list.sort()
        dup = False
        eli_list = []
        for i, [vx, vy] in enumerate(moved_list):
            if i < len(moved_list)-1:
                vnx, vny = moved_list[i+1]
                if (vx, vy) == (vnx, vny):
                    dup = True
                    continue
                else:
                    if not dup:
                        eli_list.append((vx, vy))
                    else:
                        dup = False
                        continue
            elif not dup: eli_list.append((vx, vy))
        mad_list = eli_list
    else:
        mad_list = moved_list

if not lose:
    new_board = [['.']*c for _ in range(r)]
    new_board[jx][jy] = 'I'
    for mx, my in mad_list:
        new_board[mx][my] = 'R'

    for b in new_board:
        print(''.join(b))